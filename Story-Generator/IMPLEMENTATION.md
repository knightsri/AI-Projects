# Story Generator - Implementation Guide

## Architecture Overview

The Story Generator is built on top of the `gai_lib` framework, focusing on interactive user input and story generation workflows.

## Core Implementation Strategy

### 1. Input Processing Pipeline

```python
# Interactive input gathering with validation
def gather_user_inputs():
    character = validate_required_input("Enter a character name: ")
    plot_setting = validate_required_input("Enter a plot setting: ")
    genre = validate_choice("genre", VALID_GENRES)
    audience = validate_choice("audience", VALID_AUDIENCES)
    language = process_language_input()
    # ... additional inputs
```

### 2. Prompt Engineering Strategy

#### Base Prompt Structure

```python
prompt_template = f"""
Write a short story in the {genre} genre with not less than {min_limit} 
characters and not more than {max_limit} characters with the following elements:

- Main character: {character}
- Plot Setting: {plot_setting}
- Audience: {audience}
- Output Language: {output_language}

Requirements:
- Include dialogue and descriptive language appropriate for {audience}
- Stay true to the {genre} genre throughout the story
- Create an ending that matches the {story_ending} style
- Write the story in {output_language}

CRITICAL JSON FORMATTING RULES:
- Return ONLY valid JSON - no markdown, no code blocks, no extra text
- All quotes inside the story text MUST be escaped with backslash: \\"
- All newlines should be literal \\n characters

Response format:
{{"title": "Story Title", "story": "Story content with \\"escaped quotes\\""}}
"""
```

#### Key Prompt Engineering Principles

1. **Clear Structure**: Organized requirements with bullet points
2. **Format Constraints**: Explicit JSON formatting rules to reduce parsing errors
3. **Content Guidelines**: Specific instructions for audience-appropriate content
4. **Output Format**: Standardized JSON structure for consistent processing

### 3. Multi-Provider Integration

```python
# Provider selection and execution
def execute_story_generation(prompt, api_keys, selected_providers):
    results = {}
    
    for provider in selected_providers:
        if provider in api_keys:
            print(f"Generating story using {provider}...")
            
            # Framework handles provider-specific API calls
            response = call_provider_api(provider, prompt, api_keys[provider])
            
            # Robust error handling with fallbacks
            if response and isinstance(response, dict):
                results[provider] = response
                save_story_file(provider, response, language_code)
            else:
                log_provider_error(provider, response)
                
    return results
```

### 4. Language Processing

#### Language Code Resolution

```python
def resolve_language_code(language_input):
    try:
        # Convert natural language to ISO 639-1 code
        language_code = langcodes.find(language_input).language
        if not language_code:
            raise ValueError("Language not found")
        return language_code
    except ValueError:
        print("Invalid language. Defaulting to English.")
        return langcodes.find("English").language
```

#### Supported Language Mapping

- **Input**: Natural language names ("English", "French", "German")
- **Processing**: ISO 639-1 code conversion via `langcodes` library
- **Output**: 2-letter codes for file naming (en, fr, de, etc.)

### 5. File Output Strategy

#### Filename Generation

```python
def generate_filename(provider, language_code, title):
    # Sanitize title for filesystem compatibility
    sanitized_title = "".join(
        c for c in title 
        if c.isalnum() or c in (' ', '-', '_')
    ).strip().replace(' ', '_')
    
    return f"{provider}_{language_code}_{sanitized_title}.txt"
```

#### Content Structure

```
Title: {story_title}

Story: 

{story_content}
```

## Error Handling Implementation

### 1. JSON Parsing Robustness

The implementation uses a multi-tiered parsing approach:

```python
def parse_ai_response(response_text):
    try:
        # Primary: Standard JSON parsing
        return json.loads(response_text)
    except json.JSONDecodeError:
        try:
            # Secondary: Remove markdown fences and retry
            cleaned = remove_markdown_fences(response_text)
            return json.loads(cleaned)
        except json.JSONDecodeError:
            # Tertiary: Regex extraction for known structure
            return extract_with_regex(response_text)
        except:
            # Fallback: Return error structure
            return create_error_response(response_text)
```

### 2. Input Validation

```python
# Required field validation
def validate_required_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("This field cannot be empty. Please try again.")

# Choice validation
def validate_choice(field_name, valid_options):
    while True:
        choice = input(f"Enter {field_name} {valid_options}: ")
        if choice in valid_options:
            return choice
        print(f"Invalid {field_name}. Please choose from: {valid_options}")
```

### 3. Provider Failure Handling

```python
# Continue processing even if individual providers fail
for provider in providers:
    try:
        result = generate_story(provider, prompt)
        save_result(provider, result)
        print(f"✅ {provider} completed successfully")
    except Exception as e:
        print(f"⚠️ {provider} failed: {e}")
        continue  # Process remaining providers
```

## Configuration Management

### Input Validation Constants

```python
VALID_GENRES = ['fantasy', 'sci-fi', 'mystery', 'adventure', 
               'romance', 'thriller', 'historical', 'mythological']
VALID_AUDIENCES = ['children', 'teens', 'adults']
VALID_ENDINGS = ['twist', 'cliffhanger', 'simple']
VALID_KEYS = ['All', 'GROQ', 'GEMINI', 'OPENAI']

# Character limits
MIN_CHARACTER_LIMIT = 200
MAX_CHARACTER_LIMIT = 20000
```

### Provider Priority

When "All" is selected, providers are called in this order:

1. GROQ (fastest response time)
2. GEMINI (good balance of quality/speed)  
3. OPENAI (highest quality, may have rate limits)

## Performance Considerations

### 1. Sequential Processing

- Providers are called sequentially to avoid rate limit conflicts
- Each provider result is independent and saved immediately
- Failure of one provider doesn't affect others

### 2. Response Time Optimization

- Timeout settings per provider (60 seconds default)
- Immediate file saving after each successful response
- Progress indicators for user feedback

### 3. Memory Management

- Large responses are processed and saved immediately
- No accumulation of multiple large responses in memory
- Cleanup of temporary variables after processing

## Testing Strategy

### 1. Input Validation Testing

```bash
# Test edge cases
python main.py
# Try: empty inputs, invalid genres, extreme character limits
```

### 2. Multi-Provider Testing

```bash
# Test individual providers
python main.py
# Select each provider individually to test API integrations
```

### 3. Language Processing Testing

```bash
# Test various language inputs
# "English", "français", "Deutsch", "हिंदी", etc.
```

## Future Enhancement Areas

### 1. Batch Processing

- Multiple story generation with varying parameters
- CSV input for automated story generation

### 2. Advanced Prompt Templates

- Genre-specific prompt customizations
- Audience-specific language adjustments
- Cultural context considerations

### 3. Quality Metrics

- Story length verification
- Content appropriateness checking
- Language accuracy validation

### 4. Caching Strategy

- Avoid regenerating identical prompts
- Provider response time tracking
- API usage monitoring
