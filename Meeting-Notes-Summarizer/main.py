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
    Main function for Meeting-Notes-Summarizer
    """
    print("Meeting-Notes-Summarizer starting...")
    
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
