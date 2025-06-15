import google.generativeai as genai
from config import get_api_key

def create_recipe_prompt(ingredients, cuisine, restrictions, time, skill, healthy, specialty_info):
    """
    Creates a detailed and structured prompt for the AI model.
    """
    health_preference = "The user wants a healthy version of the recipe." if healthy else "The user is open to a standard recipe."
    cuisine_preference = f"The user prefers {cuisine} cuisine." if cuisine != "Any" else "The user is open to any cuisine."

    prompt = f"""
You are an expert chef and nutritionist who creates recipes based *only* on the ingredients provided.

Your task is to generate TWO different and unique recipes based on the user's constraints.

**User Constraints:**
- **Available Ingredients:** {', '.join(ingredients)}
- **Cuisine Preference:** {cuisine_preference}
- **Dietary Needs:** {restrictions}
- **Cooking Time:** Must be achievable within {time}.
- **Skill Level:** The recipe should be suitable for a {skill} cook.
- **Health Preference:** {health_preference}
- **Pantry Notes:** {specialty_info}

Please provide the output as two distinct recipes, separated by a line containing only '---'.

For EACH recipe, please structure your response with the following markdown headings. Do NOT use any other formatting.

### Recipe Name
[Provide a creative name for the dish]

### Ingredients
[List all necessary ingredients with precise quantities. **IMPORTANT: You MUST ONLY use the ingredients from the "Available Ingredients" list provided above.** You are allowed to assume the user also has the following **basic staples ONLY**: salt, pepper, water, and cooking oil. Do NOT include any other ingredients.]

### Instructions
[Provide clear, step-by-step instructions.]

### Cooking Tips
[Offer 1-2 practical tips relevant to a {skill} cook for this recipe.]

### Substitutions
[Suggest 1-2 intelligent substitutions for key ingredients.]

### Nutritional Information
[Provide an estimated breakdown per serving for: Calories, Protein, Carbohydrates, and Fat. This section is mandatory.]
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
        error_message = str(e)
        if "API key not valid" in error_message:
            return "An error occurred: Your API key is not valid. Please check your .env file."
        return f"An error occurred: {error_message}"
