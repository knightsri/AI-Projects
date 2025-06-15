import os

def get_api_key():
    """
    Retrieves the Google AI API key from the environment variables.
    main.py is responsible for loading the .env file.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please run install.py to configure it.")
    return api_key
