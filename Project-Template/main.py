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
    Template for new AI projects.
    
    Copy this folder and modify for your specific use case.
    """
    print("Project template running...")
    
    # Example usage:
    api_keys = gai_lib.read_api_keys()
    if not api_keys:
        print("No API keys found. Check your .env file.")
        return
    
    print(f"Found API keys: {list(api_keys.keys())}")
    
    # Your project-specific code here
    # Example:
    # prompt = "Your custom prompt here"
    # response = gai_lib.call_groq_api(prompt, api_keys['GROQ'])

if __name__ == "__main__":
    main()
