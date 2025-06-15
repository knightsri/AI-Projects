import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    """
    Retrieves the Google AI API key from environment variables.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the GOOGLE_API_KEY in your .env file.")
    return api_key