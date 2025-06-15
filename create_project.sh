#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: ./create_project.sh ProjectName"
    echo "Example: ./create_project.sh Recipe-Generator"
    exit 1
fi

PROJECT_NAME=$1
PROJECT_DIR=$PROJECT_NAME

echo "Creating project: $PROJECT_NAME"

# Create project directory
mkdir -p "$PROJECT_DIR"

# Copy only the essential files from Project-Template (not the whole directory)
if [ -f "Project-Template/config.py" ]; then
    cp "Project-Template/config.py" "$PROJECT_DIR/"
fi

# Create main.py from template
cat > "$PROJECT_DIR/main.py" << 'MAIN_EOF'
import sys
import os
from pathlib import Path

# Add parent directory to path for gai_lib import
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import gai_lib

def main():
    """
    Main function for PROJECT_NAME_PLACEHOLDER
    """
    print("PROJECT_NAME_PLACEHOLDER starting...")
    
    # Read API keys
    api_keys = gai_lib.read_api_keys()
    if not api_keys:
        print("No API keys found. Check your .env file.")
        return
    
    print(f"Found API keys: {list(api_keys.keys())}")
    
    # TODO: Add your project-specific logic here
    # Example:
    # user_input = input("Enter your request: ")
    # prompt = f"Process this request: {user_input}"
    # response = gai_lib.call_groq_api(prompt, api_keys['GROQ'])
    # print(f"Response: {response}")

if __name__ == "__main__":
    main()
MAIN_EOF

# Replace placeholder in main.py
sed -i "s/PROJECT_NAME_PLACEHOLDER/$PROJECT_NAME/g" "$PROJECT_DIR/main.py"

# Create README.md from template
cat > "$PROJECT_DIR/README.md" << 'README_EOF'
# PROJECT_NAME_PLACEHOLDER

> AI-powered PROJECT_NAME_PLACEHOLDER application

## Quick Start

```bash
python main.py
```

## What This Project Does

This project uses AI to generate content related to PROJECT_NAME_PLACEHOLDER.

## Prerequisites

This project uses the shared `gai_lib` framework. See the [main project setup](../README.md) for:
- API key configuration
- Framework installation  
- Dependency management

## Usage

### Interactive Mode
```bash
python main.py
```

Follow the interactive prompts to use PROJECT_NAME_PLACEHOLDER.

## Output

Generated content is saved to files automatically.

## Development

For implementation details, see:
- 📋 **[Implementation Guide](IMPLEMENTATION.md)** - Technical details
- 🏗️ **[Framework Documentation](../README.md)** - Multi-provider AI library

## Troubleshooting

**Import Error**: Make sure you installed the package from parent directory:
```bash
cd .. && pip install -e .
```

**API Key Error**: Check your `.env` file has the correct API keys set.

## License

MIT License - feel free to use in your projects!
README_EOF

# Replace placeholders in README.md
sed -i "s/PROJECT_NAME_PLACEHOLDER/$PROJECT_NAME/g" "$PROJECT_DIR/README.md"

# Create IMPLEMENTATION.md from template
cat > "$PROJECT_DIR/IMPLEMENTATION.md" << 'IMPL_EOF'
# PROJECT_NAME_PLACEHOLDER - Implementation Guide

## Architecture Overview

The PROJECT_NAME_PLACEHOLDER is built on top of the `gai_lib` framework, focusing on content generation and processing.

## Core Implementation Strategy

### 1. Input Processing Pipeline

```python
def gather_user_inputs():
    # Interactive input gathering with validation
    # Add your input variables here
```

### 2. Prompt Engineering Strategy

```python
prompt_template = f"""
Your prompt template here

Response format:
{{"field1": "value1", "field2": "value2"}}
"""
```

### 3. Multi-Provider Integration

Uses the standard gai_lib pattern for calling multiple AI providers with error handling.

### 4. File Output Strategy

Output files are saved as: `{PROVIDER}_{PARAMS}_{IDENTIFIER}.txt`

## Configuration Management

```python
# Add your constants here
VALID_OPTIONS = ['option1', 'option2', 'option3']
```

## Testing Strategy

```bash
# Test with different inputs
python main.py
# Try: different inputs, edge cases
```

## Future Enhancement Areas

1. **Advanced Features**
2. **Performance Optimization** 
3. **User Experience Improvements**
IMPL_EOF

# Replace placeholders in IMPLEMENTATION.md
sed -i "s/PROJECT_NAME_PLACEHOLDER/$PROJECT_NAME/g" "$PROJECT_DIR/IMPLEMENTATION.md"

# Create examples directory
mkdir -p "$PROJECT_DIR/examples"

echo "✅ Created $PROJECT_NAME project"
echo "📁 Project structure:"
ls -la "$PROJECT_DIR/"
echo ""
echo "📝 Next steps:"
echo "1. cd $PROJECT_DIR"
echo "2. Edit main.py to add your project logic"
echo "3. Customize README.md and IMPLEMENTATION.md"
echo "4. Test: python main.py"