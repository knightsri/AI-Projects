# {PROJECT_NAME} - Implementation Guide

## Architecture Overview

The {PROJECT_NAME} is built on top of the `gai_lib` framework, focusing on {ARCHITECTURE_FOCUS}.

## Core Implementation Strategy

### 1. Input Processing Pipeline

```python
# {INPUT_PROCESSING_DESCRIPTION}
def gather_user_inputs():
    {INPUT_1_VAR} = validate_required_input("{INPUT_1_PROMPT}")
    {INPUT_2_VAR} = validate_required_input("{INPUT_2_PROMPT}")
    {INPUT_3_VAR} = validate_choice("{INPUT_3_NAME}", {INPUT_3_VALID_OPTIONS})
    {INPUT_4_VAR} = validate_choice("{INPUT_4_NAME}", {INPUT_4_VALID_OPTIONS})
    # ... additional inputs
```

### 2. Prompt Engineering Strategy

#### Base Prompt Structure

```python
prompt_template = f"""
{BASE_PROMPT_INSTRUCTION} with the following elements:

- {PROMPT_ELEMENT_1}: {{{PROMPT_VAR_1}}}
- {PROMPT_ELEMENT_2}: {{{PROMPT_VAR_2}}}
- {PROMPT_ELEMENT_3}: {{{PROMPT_VAR_3}}}
- {PROMPT_ELEMENT_4}: {{{PROMPT_VAR_4}}}

Requirements:
- {REQUIREMENT_1}
- {REQUIREMENT_2}
- {REQUIREMENT_3}
- {REQUIREMENT_4}

CRITICAL JSON FORMATTING RULES:
- Return ONLY valid JSON - no markdown, no code blocks, no extra text
- All quotes inside the content MUST be escaped with backslash: \\"
- {PROJECT_SPECIFIC_JSON_RULES}

Response format:
{{{JSON_RESPONSE_FORMAT}}}
"""
```

#### Key Prompt Engineering Principles

1. **Clear Structure**: {PRINCIPLE_1_DESCRIPTION}
2. **Format Constraints**: {PRINCIPLE_2_DESCRIPTION}
3. **Content Guidelines**: {PRINCIPLE_3_DESCRIPTION}
4. **Output Format**: {PRINCIPLE_4_DESCRIPTION}

### 3. Multi-Provider Integration

```python
# Provider selection and execution
def execute_{PROJECT_FUNCTION}(prompt, api_keys, selected_providers):
    results = {}
    
    for provider in selected_providers:
        if provider in api_keys:
            print(f"Processing with {provider}...")
            
            # Framework handles provider-specific API calls
            response = call_provider_api(provider, prompt, api_keys[provider])
            
            # Robust error handling with fallbacks
            if response and isinstance(response, dict):
                results[provider] = response
                save_{OUTPUT_TYPE}_file(provider, response, {SAVE_PARAMETERS})
            else:
                log_provider_error(provider, response)
                
    return results
```

### 4. {SPECIALIZED_PROCESSING_SECTION}

#### {SPECIALIZED_SUBSECTION_1}

```python
def {SPECIALIZED_FUNCTION_1}({FUNCTION_PARAMS}):
    {FUNCTION_IMPLEMENTATION}
```

#### {SPECIALIZED_SUBSECTION_2}

- **{SPECIALIZED_POINT_1}**: {DESCRIPTION_1}
- **{SPECIALIZED_POINT_2}**: {DESCRIPTION_2}
- **{SPECIALIZED_POINT_3}**: {DESCRIPTION_3}

### 5. File Output Strategy

#### Filename Generation

```python
def generate_filename(provider, {FILENAME_PARAMS}):
    # {FILENAME_SANITIZATION_DESCRIPTION}
    sanitized_{MAIN_IDENTIFIER} = "".join(
        c for c in {MAIN_IDENTIFIER} 
        if c.isalnum() or c in (' ', '-', '_')
    ).strip().replace(' ', '_')
    
    return f"{provider}_{FILENAME_PATTERN}.{FILE_EXTENSION}"
```

#### Content Structure

```
{OUTPUT_FIELD_1}: {{{FIELD_1_CONTENT}}}

{OUTPUT_FIELD_2}: 

{{{FIELD_2_CONTENT}}}
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
        result = generate_{OUTPUT_TYPE}(provider, prompt)
        save_result(provider, result)
        print(f"✅ {provider} completed successfully")
    except Exception as e:
        print(f"⚠️ {provider} failed: {e}")
        continue  # Process remaining providers
```

## Configuration Management

### Input Validation Constants

```python
{VALID_OPTIONS_1} = {VALID_LIST_1}
{VALID_OPTIONS_2} = {VALID_LIST_2}
{VALID_OPTIONS_3} = {VALID_LIST_3}
{VALID_OPTIONS_4} = {VALID_LIST_4}

# {PROJECT_SPECIFIC_LIMITS}
{LIMIT_1_NAME} = {LIMIT_1_VALUE}
{LIMIT_2_NAME} = {LIMIT_2_VALUE}
```

### Provider Priority

When "All" is selected, providers are called in this order:

1. GROQ ({GROQ_PRIORITY_REASON})
2. GEMINI ({GEMINI_PRIORITY_REASON})  
3. OPENAI ({OPENAI_PRIORITY_REASON})

## Performance Considerations

### 1. Sequential Processing

- {PERFORMANCE_POINT_1}
- {PERFORMANCE_POINT_2}
- {PERFORMANCE_POINT_3}

### 2. Response Time Optimization

- {OPTIMIZATION_POINT_1}
- {OPTIMIZATION_POINT_2}
- {OPTIMIZATION_POINT_3}

### 3. Memory Management

- {MEMORY_POINT_1}
- {MEMORY_POINT_2}
- {MEMORY_POINT_3}

## Testing Strategy

### 1. Input Validation Testing

```bash
# Test edge cases
python main.py
# Try: {TESTING_SCENARIOS}
```

### 2. Multi-Provider Testing

```bash
# Test individual providers
python main.py
# Select each provider individually to test API integrations
```

### 3. {PROJECT_SPECIFIC_TESTING_SECTION}

```bash
# {TESTING_DESCRIPTION}
# {TESTING_EXAMPLES}
```

## Future Enhancement Areas

### 1. {ENHANCEMENT_AREA_1}

- {ENHANCEMENT_1_POINT_1}
- {ENHANCEMENT_1_POINT_2}

### 2. {ENHANCEMENT_AREA_2}

- {ENHANCEMENT_2_POINT_1}
- {ENHANCEMENT_2_POINT_2}

### 3. {ENHANCEMENT_AREA_3}

- {ENHANCEMENT_3_POINT_1}
- {ENHANCEMENT_3_POINT_2}

### 4. {ENHANCEMENT_AREA_4}

- {ENHANCEMENT_4_POINT_1}
- {ENHANCEMENT_4_POINT_2}
