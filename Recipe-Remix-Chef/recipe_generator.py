import google.generativeai as genai
from config import get_api_key

def create_recipe_prompt(ingredients, restrictions, time, skill):
    """
    Creates a detailed and structured prompt for the AI model.
    """
    prompt = f"""
You are an expert chef specializing in innovative vegan and vegetarian (no egg) cuisine.
Your task is to generate a unique recipe based on the user's constraints.

**User Constraints:**
- **Available Ingredients:** {', '.join(ingredients)}
- **Dietary Needs:** {restrictions} (ensure the recipe is strictly egg-free)
- **Cooking Time:** Must be achievable within {time}.
- **Skill Level:** The recipe should be suitable for a {skill} cook.

**Recipe Output Format:**
Please structure your response with the following markdown headings:

### Recipe Name
[Provide a creative name for the dish]

### Ingredients
[List all necessary ingredients with precise quantities. You may include common pantry staples.]

### Instructions
[Provide clear, step-by-step instructions from start to finish.]

### Cooking Tips
[Offer 1-2 practical tips relevant to a {skill} cook for this specific recipe.]

### Substitutions
[Suggest 1-2 intelligent substitutions for key ingredients.]
"""
    return prompt

def generate_recipe(prompt):
    """
    Sends the prompt to the Google AI model and returns the generated recipe.
    """
    try:
        api_key = get_api_key()
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"