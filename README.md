# AI Projects Framework

> Multi-provider AI library with project templates for rapid development

## Overview

A flexible Python framework for building AI applications that work with multiple providers (GROQ, GEMINI, OpenAI). Includes working projects and templates for quick development.

## Quick Start

```bash
# Install the framework
pip install -e .

# Create a new project
./create_project.sh My-New-AI-Project

# Run an existing project
cd Story-Generator
python main.py
```

## Framework Features

- 🤖 **Multi-Provider Support**: GROQ, GEMINI, and OpenAI APIs
- 🛡️ **Robust Error Handling**: Graceful fallbacks and JSON parsing
- 📦 **Package Structure**: Professional Python package with proper dependencies
- 🚀 **Project Templates**: Quick setup for new AI projects
- ⚙️ **Centralized Config**: Single `.env` file for all API keys
- 🔄 **Consistent Interface**: Standardized API calls across providers

## Included Projects

| Project | Description | Status |
|---------|-------------|--------|
| **Story-Generator** | Interactive story creation with customizable parameters | ✅ Complete |
| **Career-Advice-Counselor** | AI-powered career guidance (template) | 🏗️ Template |
| **Meeting-Notes-Summarizer** | Meeting content summarization (template) | 🏗️ Template |
| **Personal-Learning-Tutor** | Personalized learning assistance (template) | 🏗️ Template |
| **Recipe-Remix-Chef** | Recipe generation and modification (template) | 🏗️ Template |

## Setup

### 1. Install Dependencies
```bash
pip install -e .
```

### 2. Configure API Keys
Create `.env` file with your API keys:
```bash
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_google_api_key_here  
OPENAI_API_KEY=your_openai_api_key_here
```

**Get API Keys:**
- [GROQ Console](https://console.groq.com/)
- [Google AI Studio](https://aistudio.google.com/) (for Gemini)
- [OpenAI Platform](https://platform.openai.com/)

### 3. Test Installation
```bash
python -c "import gai_lib; print('✅ Framework ready!')"
```

## Usage

### Using the Framework in Your Code
```python
import gai_lib

# Read API keys
api_keys = gai_lib.read_api_keys()

# Generate content
prompt = "Your AI prompt here"
response = gai_lib.call_groq_api(prompt, api_keys['GROQ'])
print(response['title'], response['story'])
```

### Creating New Projects
```bash
# Use the project generator
./create_project.sh Recipe-Generator

# Or copy the template manually
cp -r Project-Template/ My-Project/
cd My-Project/
# Edit main.py, README.md, IMPLEMENTATION.md
```

## Project Structure

```
├── .env                     # API keys (create this)
├── gai_lib/                 # Core framework package
│   ├── core.py              # Main API functions
│   ├── providers/           # Provider-specific implementations (future)
│   └── utils/               # Helper utilities (future)
├── Story-Generator/         # Working story generation project
├── Project-Template/        # Template for new projects
├── docs/                    # Framework documentation
├── create_project.sh        # Project creation script
├── setup.py                 # Package configuration
└── requirements.txt         # Dependencies
```

## API Reference

### Core Functions
```python
# API key management
api_keys = gai_lib.read_api_keys()

# Provider calls
response = gai_lib.call_groq_api(prompt, api_key)
response = gai_lib.call_gemini_api(prompt, api_key)  
response = gai_lib.call_openai_api(prompt, api_key)

# JSON parsing (with fallbacks)
data = gai_lib.parse_llm_json(response_text)
```

### Response Format
All provider functions return standardized dictionaries:
```python
{
    "title": "Generated Title",
    "story": "Generated content...",
    # Additional fields depending on prompt
}
```

## Error Handling

The framework includes multiple layers of error handling:

- **JSON Parsing**: Multiple fallback methods for malformed responses
- **Provider Failures**: Continue with remaining providers if one fails
- **Network Issues**: Timeout handling and retry logic
- **Input Validation**: User input validation for all projects

## Development

### Adding New Providers
1. Add API integration to `gai_lib/core.py`
2. Follow the existing pattern for error handling
3. Update `VALID_KEYS` in project templates

### Framework Architecture
For detailed technical information, see [IMPLEMENTATION.md](IMPLEMENTATION.md).

### Contributing
1. Fork the repository
2. Create a feature branch
3. Test with multiple providers
4. Submit a pull request

## Dependencies

- `groq` - GROQ API client
- `google-genai`, `google-generativeai` - Google Gemini APIs
- `openai==0.27.10` - OpenAI API client
- `requests` - HTTP client
- `python-dotenv` - Environment variable management
- `langcodes` - Language code handling

## Examples

### Story Generation
```bash
cd Story-Generator
python main.py
# Follow prompts: character, setting, genre, etc.
# Output: GROQ_en_Adventure_Story.txt
```

### Custom Project
```bash
./create_project.sh Weather-Reporter
cd Weather-Reporter
# Edit main.py with weather-specific logic
python main.py
```

## Troubleshooting

**Import Error**: Run `pip install -e .` from the main directory  
**API Key Error**: Check your `.env` file has the correct format  
**JSON Parse Error**: Framework has fallbacks - check output files for content  

## License

MIT License - feel free to use in your projects!

---

**Author**: knightsri  
**Version**: 1.0.0  
**Repository**: https://github.com/knightsri/AI-Projects