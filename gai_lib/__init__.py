"""
GAI-Lib: Multi-provider AI library for various projects
"""

# Import all functions from core module to make them available at package level
from .core import (
    read_api_keys,
    parse_llm_json,
    call_groq_api,
    call_gemini_api,
    call_openai_api
)

# Package metadata
__version__ = "1.0.0"
__author__ = "knightsri <>"

# Make functions available when importing gai_lib
__all__ = [
    'read_api_keys',
    'parse_llm_json', 
    'call_groq_api',
    'call_gemini_api',
    'call_openai_api'
]
