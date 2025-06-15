"""
Project-specific configuration template.
Copy and modify for each new project.
"""

# Project metadata
PROJECT_NAME = "template"
PROJECT_DESCRIPTION = "Template for new AI projects"

# Default settings
DEFAULT_GENRE = "fantasy"
DEFAULT_AUDIENCE = "adults"
DEFAULT_LANGUAGE = "English"

# Story parameters (adjust as needed)
MIN_CHARACTER_LIMIT = 200
MAX_CHARACTER_LIMIT = 20000

# Valid options (customize for your project)
VALID_GENRES = ['fantasy', 'sci-fi', 'mystery', 'adventure', 'romance', 'thriller', 'historical', 'mythological']
VALID_AUDIENCES = ['children', 'teens', 'adults']
VALID_ENDINGS = ['twist', 'cliffhanger', 'simple']
VALID_KEYS = ['All', 'GROQ', 'GEMINI', 'OPENAI']

# Project-specific prompt templates
PROMPT_TEMPLATE = """
Your project-specific prompt template here.
Use variables like {genre}, {character}, etc.
"""
