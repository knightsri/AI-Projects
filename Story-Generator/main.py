import sys
import os
from pathlib import Path

# Add parent directory to path for gai_lib import
sys.path.insert(0, str(Path(__file__).parent.parent))

import sys
import os
import langcodes
import json
from dotenv import load_dotenv, find_dotenv

# Ensure the parent directory is in the system path to import gai_lib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gai_lib

# The .env is one level up from main.py
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Read API keys using the gai_lib module
api_keys = gai_lib.read_api_keys()

# If no api_keys are found, print a message and exit
if not api_keys:
    print("No API keys found. Please set the environment variables ending with '_API_KEY'.")
    sys.exit(1)

# Do this only if debugging is needed
# Uncomment the following lines to print the API keys for debugging purposes
## Print the API keys to verify they are read correctly
#for key, value in api_keys.items():
#    print(f"{key}: {value}")


# Gather all the input from the user

# Validate the input for character name and setting and ensure they are not empty
while True:
    if not (character := input("Enter a character name: ").strip()):
        print("Character name cannot be empty. Please try again.")
    elif not (plot_setting := input("Enter a plot setting for your story: ").strip()):
        print("Plot setting cannot be empty. Please try again.")
    else:
        break

# Validate the input for genre and ensure it is one of the valid genres
valid_genres = ['fantasy', 'sci-fi', 'mystery', 'adventure', 'romance', 'thriller', 'historical', 'mythological']
genre = input(f"Enter a genre {valid_genres}: ")
while genre not in valid_genres:
    print(f"Invalid genre. Please choose from: {valid_genres}")
    genre = input(f"Enter a genre {valid_genres}: ")

# Validate the input for audience and ensure it is one of the valid audiences
valid_audiences = ['children', 'teens', 'adults']
audience = input(f"Enter an audience {valid_audiences}: ")
while audience not in valid_audiences:
    print(f"Invalid audience. Please choose from: {valid_audiences}")
    audience = input(f"Enter an audience {valid_audiences}: ")

# Validate the output language and ensure it is not empty
language_code = None
while True:
    output_language = input("Enter an output language: ")
    if output_language.strip():
        break
    print("Output language cannot be empty. Please try again.")
    
# Find or calculate language code from ISO 639-1 standard
# For example, 'en' for English, 'fr' for French, etc.
try:
    # Convert language name to ISO 639-1 2-letter code
    # This will raise ValueError if the language is not found
    language_code = langcodes.find(output_language).language
    if not language_code:
        raise ValueError("Language not found in ISO 639-1 standard.")
except ValueError:
    print("Invalid language name. Defaulting to English.")
    language_code = langcodes.find("English").language


# Validate the input for keys to use and ensure it is one of the valid options
valid_keys = ['All', 'GROQ', 'GEMINI', 'OPENAI']
key_to_use = input(f"Enter key to use {valid_keys}: ")
while key_to_use not in valid_keys:
    print(f"Invalid keys. Please choose from: {valid_keys}")
    key_to_use = input(f"Enter key to use {valid_keys}: ")

# Validate the input for story length and ensure it is a positive integer and is between the limits
min_limit = MINCHARACTER_LIMIT = 200
max_limit = MAXCHARACTER_LIMIT = 20000 
while True:
    # Prompt the user for both minimum and maximum character limits on the story
    min_limit = input(f"Enter the minimum character limit for the story (default {MINCHARACTER_LIMIT}): ")
    if not min_limit.strip():
        min_limit = MINCHARACTER_LIMIT
    else:
        try:
            min_limit = int(min_limit)
            if min_limit < MINCHARACTER_LIMIT :
                raise ValueError("Minimum limit is less than the allowed minimum.")
            elif min_limit > MAXCHARACTER_LIMIT:
                raise ValueError("Minimum limit is greater than the allowed maximum.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer greater than or equal to {MINCHARACTER_LIMIT}.")
            continue
    
    # Prompt the user for the maximum character limit on the story
    max_limit = input(f"Enter the maximum character limit for the story (default {MAXCHARACTER_LIMIT}): ")
    if not max_limit.strip():
        max_limit = MAXCHARACTER_LIMIT
    else:
        try:
            max_limit = int(max_limit)
            if max_limit > MAXCHARACTER_LIMIT:
                raise ValueError("Maximum limit is greater than the allowed maximum.")
            elif max_limit < min_limit:
                raise ValueError("Maximum limit is less than the minimum limit.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer less than or equal to {MAXCHARACTER_LIMIT}.")
            continue
    # If both limits are valid, break the loop
    if min_limit <= max_limit:
        break
   

# Validate the input for story ending and ensure it is one of the valid endings
valid_endings = ['twist', 'cliffhanger', 'simple']
story_ending = input(f"Enter the ending of the story {valid_endings}: ")
while story_ending not in valid_endings:
    print(f"Invalid ending. Please choose from: {valid_endings}")
    story_ending = input(f"Enter the ending of the story {valid_endings}: ")

# Generate the prompt for the AI story generator
# Generate the prompt for the AI story generator
# Generate the prompt for the AI story generator
prompt = f"""
Write a short story in the {genre} genre with not less than {min_limit} characters and not more than {max_limit} characters. Use the following elements:

- Main character: {character}
- Plot Setting: {plot_setting}
- Target Audience: {audience}
- Language: {output_language}
- Story Ending Style: {story_ending}

Requirements:
- Include dialogue and descriptive language appropriate for {audience}
- Stay true to the {genre} genre throughout the story
- Create an ending that matches the {story_ending} style
- Write the story in {output_language}

CRITICAL JSON FORMATTING RULES:
- Return ONLY valid JSON - no markdown, no code blocks, no extra text
- All quotes inside the story text MUST be escaped with backslash: \\"
- All newlines should be literal \\n characters
- Do not use any control characters that break JSON

Example format:
{{"title": "Story Title", "story": "Story text with \\"escaped quotes\\" and proper formatting."}}

Your response:
"""

# Print the generated prompt for debugging purposes
print("Generated Prompt:")
print(prompt)

# If key_to_use is 'All', use all available API keys in api_keys
keys_to_use = []
if key_to_use == 'All':
    keys_to_use = list(api_keys.keys())
# else, use only the specified key API_{key_to_use.upper()}
else:
    key_to_use = key_to_use.upper()
    # Convert the single key to a list
    keys_to_use = [f"{key_to_use}"]

# For each of the API keys in keys_to_use, do the following:
# Call the respective API and generate a story
for key in keys_to_use:
    if key in api_keys:
        # print(f"Calling API with key: {key} and value: {api_keys[key]}")
        # Generate the story using the API key
        print(f"Generating story using {key}...")

        # Call the respective API based on the key
        response = None
        api_key = api_keys[key]
        
        if key == 'GROQ':
            # Call the GROQ API
            response = gai_lib.call_groq_api(prompt, api_key)
        elif key == 'GEMINI':
            # Call the GEMINI API
            response = gai_lib.call_gemini_api(prompt, api_key)
        elif key == 'OPENAI':
            # Call the OpenAI API
            response = gai_lib.call_openai_api(prompt, api_key)
        else:
            print(f"Unknown API key: {key}")
            continue

        # Print the response for debugging purposes
        print(f"Response from {key}: success={response is not None}")
        if response:
            print(f"  Title: {response.get('title', 'N/A')}")
            print(f"  Story length: {len(response.get('story', ''))} characters")

        # Ensure response is a dictionary
        if not isinstance(response, dict):
            print(f"Error: {key} API did not return a dictionary. Got: {type(response)}")
            continue

        # Extract the "title" and "story" from the response dictionary
        title = response.get("title", "Untitled")
        story = response.get("story", "No story content available")

        # Sanitize the title to create a valid filename
        sanitized_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')

        # Save the response to a file name {key}_{language_code}_{sanitized_title}.txt
        filename = f"{key}_{language_code}_{sanitized_title}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\n\n")
                f.write(f"Story: \n\n{story}")
            print(f"Response from {key} saved to {filename}")
        except Exception as e:
            print(f"Error saving file {filename}: {e}")
    else:
        print(f"API key for {key} not found in environment variables")

print("\nStory generation completed!")