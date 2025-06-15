# gai_lib.py
"""
This module provides functions to interact with various Generative AI APIs like GROQ, GEMINI, and OpenAI.
It includes functions to read API keys from environment variables, parse JSON responses, and call the respective APIs.
"""

import os
import requests
import google.genai as genai
from google.genai.types import HarmCategory, HarmBlockThreshold
from google.auth.exceptions import RefreshError as GoogleAuthRefreshError
from google.api_core.exceptions import GoogleAPIError, DeadlineExceeded
from google.generativeai import GenerativeModel
import google.generativeai as old_genai  # For configure method
import openai
import json

# Read API keys from the environment variables
# The keys are defined as: GROQ_API_KEY, GOOGLE_API_KEY etc.
# Read all the keys in the environment variables and save them to an associated dictionary and return the same
def read_api_keys():
    api_keys = {}
    for key, value in os.environ.items():
        if key.endswith("_API_KEY"):
            # strip the suffix '_API_KEY' to get the service name
            key = key[:-len("_API_KEY")].upper()
            api_keys[key] = value
    return api_keys


# Parse the LLM response text to extract JSON data
# This function is designed to handle common issues with LLM responses that are supposed to be JSON.
def parse_llm_json(llm_text_response):
    # 1. Strip leading/trailing whitespace
    cleaned_text = llm_text_response.strip()

    # 2. Remove markdown code block fences if present
    # Handle both ```json and ``` cases
    if cleaned_text.startswith('```json'):
        cleaned_text = cleaned_text[len('```json'):]
    elif cleaned_text.startswith('```'):
        cleaned_text = cleaned_text[len('```'):]
    
    if cleaned_text.endswith('```'):
        cleaned_text = cleaned_text[:-len('```')]

    # Strip again in case removing fences left new leading/trailing whitespace
    cleaned_text = cleaned_text.strip()

    # 3. Attempt to parse the cleaned text
    try:
        data = json.loads(cleaned_text)
        return data
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Attempting to fix common JSON issues...")
        
        # Try to fix common issues with AI-generated JSON
        try:
            # Method 1: Try using json.loads with strict=False (allows control chars)
            data = json.loads(cleaned_text, strict=False)
            print("Successfully parsed with strict=False")
            return data
        except:
            pass
            
        try:
            # Method 2: Manual extraction if it looks like a simple title/story structure
            import re
            
            # Look for title and story fields using regex
            title_match = re.search(r'"title"\s*:\s*"([^"]*(?:\\.[^"]*)*)"', cleaned_text, re.DOTALL)
            story_match = re.search(r'"story"\s*:\s*"([^"]*(?:\\.[^"]*)*)"', cleaned_text, re.DOTALL)
            
            if title_match and story_match:
                title = title_match.group(1)
                story = story_match.group(1)
                
                # Unescape common escape sequences
                title = title.replace('\\"', '"').replace('\\n', '\n').replace('\\t', '\t')
                story = story.replace('\\"', '"').replace('\\n', '\n').replace('\\t', '\t')
                
                print("Successfully extracted using regex parsing")
                return {"title": title, "story": story}
        except Exception as regex_error:
            print(f"Regex extraction failed: {regex_error}")
        
        # If all methods fail, return the error with the raw content
        print(f"All parsing methods failed. Original error: {e}")
        print(f"Problematic JSON string (start): {cleaned_text[:200]}...") 
        print(f"Problematic JSON string (end): ...{cleaned_text[-200:]}")
        
        # Return a fallback response instead of crashing
        return {
            "title": "JSON Parse Error", 
            "story": f"Could not parse response as JSON. Raw content: {cleaned_text}"
        }
    except Exception as e:
        print(f"An unexpected error occurred during JSON parsing: {e}")
        return {
            "title": "Unexpected Parse Error", 
            "story": f"Unexpected error during parsing: {e}. Raw content: {cleaned_text}"
        }


# Implementation for call_groq_api
DEFAULT_GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
DEFAULT_GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"  # Hypothetical endpoint, adjust as needed
def call_groq_api(prompt, api_key, apiend_point=DEFAULT_GROQ_ENDPOINT, model_name=DEFAULT_GROQ_MODEL) -> dict:
    """
    Calls the GROQ API with the provided prompt and API key.

    Args:
        prompt (str): The prompt to send to the API.
        api_key (str): The API key for authentication.
        model_name (str, optional): The name of the model to use.
                                    Defaults to "meta-llama/llama-4-scout-17b-16e-instruct".

    Returns:
        dict: The parsed JSON response with title and story keys.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print(f"Calling GROQ API with model: {model_name} and endpoint: {apiend_point}, prompt length: {len(prompt)} characters")

    payload = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1500,
        "temperature": 0.7,
        "top_p": 0.9,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "stop": None,
        "stream": False 
    }

    try:
        response = requests.post(apiend_point, json=payload, headers=headers, timeout=60)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)

        # Parse the response
        response_data = response.json()
        
        # Extract the content from the response
        if response_data.get("choices") and len(response_data["choices"]) > 0:
            content = response_data["choices"][0].get("message", {}).get("content")
            if content:
                try:
                    # Parse the JSON content returned by the AI
                    return parse_llm_json(content)
                except (json.JSONDecodeError, Exception) as e:
                    print(f"Error parsing GROQ response as JSON: {e}")
                    print(f"Raw content: {content}")
                    return {"title": "JSON Parse Error", "story": f"Could not parse response as JSON: {content}"}
            else:
                return {"title": "No Content", "story": "No content generated by Groq API."}
        else:
            return {"title": "Unexpected Response", "story": f"Unexpected Groq API response format: {response_data}"}

    except requests.exceptions.HTTPError as http_err:
        return {"title": "HTTP Error", "story": f"HTTP error occurred: {http_err}. Response: {response.text}"}
    except requests.exceptions.ConnectionError as conn_err:
        return {"title": "Connection Error", "story": f"Connection error: {conn_err}"}
    except requests.exceptions.Timeout as timeout_err:
        return {"title": "Timeout Error", "story": f"Request timed out: {timeout_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"title": "Request Error", "story": f"Request error: {req_err}"}
    except Exception as e:
        return {"title": "Unexpected Error", "story": f"Unexpected error: {e}"}

# Implementation for call_gemini_api
DEFAULT_GEMINI_MODEL = "gemini-1.5-flash-latest" # Using a common and efficient model
def call_gemini_api(prompt: str, api_key, model_name: str = DEFAULT_GEMINI_MODEL) -> dict:
    """
    Calls the GEMINI Generative AI API with the provided prompt and API key.

    Args:
        prompt (str): The prompt to send to the API.
        api_key (str): The API key for authentication.
        model_name (str, optional): The name of the Gemini model to use.
                                    Defaults to "gemini-1.5-flash-latest".

    Returns:
        dict: The parsed JSON response with title and story keys.
    """
    try:
        # Configure the client library with your API key
        # Note: This might not be needed if you're configuring elsewhere
        # genai.configure(api_key=api_key)
        
        # Initialize the generative model
        model = GenerativeModel(model_name)
        
        # Optional: Define generation configuration
        generation_config = genai.types.GenerationConfig(
            max_output_tokens=1500,
            temperature=0.7,
            top_p=0.9,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=None
        )

        print(f"Calling GEMINI API with model: {model_name}, prompt length: {len(prompt)} characters")

        # Make the API call
        response = model.generate_content(
            prompt,
            # safety_settings=safety_settings,
            request_options={"timeout": 60}  # Set a timeout for the API request (in seconds)
        )

        # Accessing the generated text:
        # The .text property is a convenient way to get the model's response.
        if response.text:
            return parse_llm_json(response.text.strip())  # Parse the response text as JSON
        else:
            # If response.text is empty, try to get more details
            error_details = []
            if response.prompt_feedback:
                if response.prompt_feedback.block_reason:
                    error_details.append(f"Blocked due to: {response.prompt_feedback.block_reason.name}")
                for rating in response.prompt_feedback.safety_ratings:
                    if rating.blocked:
                         error_details.append(f"Prompt safety rating blocked: {rating.category.name}")
            
            if response.candidates:
                for candidate in response.candidates:
                    if candidate.finish_reason and candidate.finish_reason.name not in ["STOP", "UNSPECIFIED"]:
                        error_details.append(f"Candidate finished due to: {candidate.finish_reason.name}")
                    if hasattr(candidate, 'safety_ratings'):
                        for rating in candidate.safety_ratings:
                            if rating.blocked:
                                error_details.append(f"Candidate safety rating blocked: {rating.category.name}")
            
            if not error_details:
                error_details.append("No text content in response and no specific block/finish reason found.")
            
            return {"title": "GEMINI API Error", "story": "No content generated by GEMINI API.\n\nDetails:\n\n" + "\n\n".join(error_details)}

    except GoogleAuthRefreshError as auth_err:
        return {"title": "GEMINI API Authentication Error", "story": "Ensure your API key is valid and has the necessary permissions.\n\nDetails:\n\n" + str(auth_err)}
    except DeadlineExceeded:
        return {"title": "GEMINI API Timeout Error", "story": "GEMINI API request timed out. Please try again later or with a shorter prompt."}
    except GoogleAPIError as api_err:
        return {"title": "GEMINI API Error", "story": f"GEMINI API error occurred: {api_err}"}
    except AttributeError as attr_err:
        return {"title": "GEMINI API Response Error", "story": f"Error processing GEMINI API response (AttributeError): {attr_err}. This could be due to an unexpected response format or an issue with the SDK setup."}
    except Exception as e:
        return {"title": "GEMINI API Unexpected Error", "story": f"An unexpected error occurred while calling GEMINI API: {type(e).__name__} - {e}"}

# Implementation for call_openai_api
DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo"
def call_openai_api(prompt: str, api_key: str, model_name: str = DEFAULT_OPENAI_MODEL) -> dict:
    """
    Calls the OpenAI API with the provided prompt and API key.

    Args:
        prompt (str): The prompt to send to the API.
        api_key (str): The API key for authentication.
        model_name (str, optional): The name of the OpenAI model to use.
                                   Defaults to "gpt-3.5-turbo".

    Returns:
        dict: The parsed JSON response with title and story keys.
    """
    try:
        print(f"Calling OPENAI API with model: {model_name}, prompt length: {len(prompt)} characters")

        # Set the API key for OpenAI v0.27.10
        openai.api_key = api_key
        
        # Make the API call using the v0.27.10 format
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7,
            top_p=0.9,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract the content from the response
        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            if content:
                try:
                    return parse_llm_json(content)
                except (json.JSONDecodeError, Exception) as e:
                    print(f"Error parsing OpenAI response as JSON: {e}")
                    print(f"Raw content: {content}")
                    return {"title": "JSON Parse Error", "story": f"Could not parse response as JSON: {content}"}
            else:
                return {"title": "No Content", "story": "No content generated by OpenAI API."}
        else:
            return {"title": "Unexpected Response", "story": "Unexpected OpenAI API response format"}

    except openai.error.AuthenticationError as e:
        return {"title": "OpenAI Authentication Error", "story": f"Authentication failed. Check your API key: {e}\n\nAPI KEY: {api_key}"}
    except openai.error.RateLimitError as e:
        return {"title": "OpenAI Rate Limit", "story": f"Rate limit exceeded: {e}"}
    except openai.error.APIError as e:
        return {"title": "OpenAI API Error", "story": f"OpenAI API error: {e}"}
    except openai.error.Timeout as e:
        return {"title": "OpenAI Timeout Error", "story": f"Request timed out: {e}"}
    except openai.error.APIConnectionError as e:
        return {"title": "OpenAI Connection Error", "story": f"Failed to connect to OpenAI: {e}"}
    except openai.error.InvalidRequestError as e:
        return {"title": "OpenAI Invalid Request", "story": f"Invalid request: {e}"}
    except Exception as e:
        return {"title": "OpenAI Unexpected Error", "story": f"An unexpected error occurred while calling OpenAI API: {type(e).__name__} - {e}"}