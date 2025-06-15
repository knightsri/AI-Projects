# AI Projects Framework - Implementation Guide

## Architecture Overview

A modular Python framework designed for rapid AI application development with multiple provider support and standardized interfaces.

## Framework Design Principles

### 1. **Provider Abstraction**

All AI providers return standardized response formats, allowing seamless switching between GROQ, GEMINI, and OpenAI.

### 2. **Error Resilience**

Multi-tiered error handling ensures applications continue working even when individual providers fail.

### 3. **Development Velocity**

Project templates and consistent patterns enable rapid prototyping of AI applications.

## Core Components

### Package Structure

```
gai_lib/
├── __init__.py          # Package interface - exports all functions
├── core.py              # Main implementation - all provider APIs
├── providers/           # Future: separate provider implementations
└── utils/               # Future: helper utilities
```

### Key Functions

```python
# gai_lib/__init__.py - Public API
from .core import (
    read_api_keys,        # Environment variable management
    parse_llm_json,       # Robust JSON parsing with fallbacks
    call_groq_api,        # GROQ provider integration
    call_gemini_api,      # GEMINI provider integration  
    call_openai_api       # OpenAI provider integration
)
```

## Provider Implementation Pattern

### Standardized Return Format

```python
def call_provider_api(prompt: str, api_key: str) -> dict:
    """
    All providers follow this pattern:
    1. Configure client with API key
    2. Make API call with standardized parameters
    3. Parse response with error handling
    4. Return standardized dict format
    """
    try:
        # Provider-specific API call
        response = provider_client.generate(prompt, **config)
        
        # Parse JSON content with fallbacks
        return parse_llm_json(response.content)
        
    except ProviderError as e:
        return {"title": "Provider Error", "story": f"Error: {e}"}
```

### Error Handling Strategy

```python
# Multi-tiered JSON parsing
def parse_llm_json(response_text):
    try:
        return json.loads(response_text)                    # Standard parsing
    except json.JSONDecodeError:
        try:
            cleaned = remove_markdown_fences(response_text)
            return json.loads(cleaned)                      # Markdown removal
        except json.JSONDecodeError:
            return extract_with_regex(response_text)        # Regex fallback
        except:
            return create_error_response(response_text)     # Safe fallback
```

## Project Template System

### Template Structure

```
Project-Template/
├── main.py              # Boilerplate with gai_lib imports
├── config.py            # Project-specific configuration
├── README.md            # User-focused documentation
└── doc-templates/       # README and IMPLEMENTATION templates
```

### Project Creation Workflow

```bash
./create_project.sh NewProject
# 1. Creates directory structure
# 2. Generates main.py with imports configured
# 3. Creates README.md and IMPLEMENTATION.md from templates
# 4. Sets up examples/ directory
```

## Configuration Management

### Environment Variables

```python
# gai_lib/core.py
def read_api_keys():
    """Scan environment for *_API_KEY variables"""
    api_keys = {}
    for key, value in os.environ.items():
        if key.endswith("_API_KEY"):
            service = key[:-len("_API_KEY")].upper()
            api_keys[service] = value
    return api_keys
```

### Centralized .env Loading

```python
# All projects use this pattern
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())  # Searches up directory tree for .env
```

## Provider-Specific Implementations

### GROQ API Integration

```python
# Uses requests library with OpenAI-compatible endpoint
def call_groq_api(prompt, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1500, "temperature": 0.7
    }
    response = requests.post(GROQ_ENDPOINT, json=payload, headers=headers)
```

### GEMINI API Integration  

```python
# Uses dual-package approach for compatibility
import google.genai as genai                    # New package (types)
import google.generativeai as old_genai        # Old package (configure/model)

def call_gemini_api(prompt, api_key):
    old_genai.configure(api_key=api_key)        # Configuration
    model = GenerativeModel(model_name)         # Model from old package
    response = model.generate_content(prompt)   # Generation
```

### OpenAI API Integration

```python
# Compatible with OpenAI v0.27.10
def call_openai_api(prompt, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
```

## Development Patterns

### Project Main Structure

```python
# Standard pattern for all projects
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import gai_lib

def main():
    # 1. Gather user inputs with validation
    # 2. Create AI prompt from inputs  
    # 3. Call provider(s) via gai_lib
    # 4. Process and save responses
```

### Input Validation Pattern

```python
def validate_required_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("This field cannot be empty. Please try again.")

def validate_choice(field_name, valid_options):
    while True:
        choice = input(f"Enter {field_name} {valid_options}: ")
        if choice in valid_options:
            return choice
        print(f"Invalid {field_name}. Please choose from: {valid_options}")
```

## Performance Considerations

### Sequential Provider Calls

- Providers called sequentially to avoid rate limits
- Each provider result saved immediately
- Independent error handling per provider

### Memory Management

- Large responses processed and saved immediately
- No accumulation of multiple responses in memory
- Cleanup after each provider call

### Timeout Handling

- 60-second timeout per provider by default
- Graceful degradation on timeout
- User feedback during long operations

## Testing Strategy

### Framework Testing

```python
# Test API key loading
api_keys = gai_lib.read_api_keys()
assert len(api_keys) > 0

# Test provider calls
response = gai_lib.call_groq_api("Test prompt", api_keys['GROQ'])
assert isinstance(response, dict)
assert 'title' in response or 'story' in response
```

### Project Testing

```bash
# Each project should support:
python main.py  # Interactive testing
# Test edge cases: empty inputs, invalid options, extreme parameters
```

## Future Architecture Plans

### Provider Separation

```
gai_lib/
├── providers/
│   ├── groq.py          # Isolated GROQ implementation
│   ├── gemini.py        # Isolated GEMINI implementation
│   └── openai.py        # Isolated OpenAI implementation
├── utils/
│   ├── json_parser.py   # JSON parsing utilities
│   └── config.py        # Configuration management
└── factory.py           # Provider factory pattern
```

### Enhanced Error Handling

- Provider-specific retry strategies
- Rate limiting detection and backoff
- Health checking for provider availability

### Advanced Features

- Caching layer for repeated prompts
- Usage tracking and cost monitoring  
- Batch processing capabilities
- Streaming response support

## Deployment Considerations

### Package Installation

```python
# setup.py ensures all dependencies installed
pip install -e .  # Development mode
pip install .     # Production installation
```

### Environment Management

- `.env` file for development
- Environment variables for production
- API key validation on startup

### Error Monitoring

- Structured error responses
- Provider failure logging
- Performance metrics collection
