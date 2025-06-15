import os
import sys

# Import packages, assuming they were installed by the setup script
try:
    from dotenv import load_dotenv
    from recipe_generator import create_recipe_prompt, generate_recipe
    from utils import format_recipe
except ImportError:
    print("Error: Required packages are not installed.")
    print("Please run the setup script first to install dependencies:")
    if sys.platform == "win32":
        print("   python install.py")
    else:
        print("   python3 install.py")
    sys.exit(1)

# Load the environment variables from the .env file created by install.py
load_dotenv()

# --- Main Application Logic ---
if __name__ == "__main__":
    print("--- Initializing Recipe-Remix-Chef ---\n")

    def get_recipe_inputs():
        """
        Gathers all necessary inputs from the user.
        """
        print("🌿 Welcome! 🌿")
        print("Let's create a delicious recipe with the ingredients you have.\n")

        ingredients_input = input("Enter your available ingredients (comma-separated): ")
        ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]

        restrictions = input("Any dietary restrictions? (e.g., non-veg, vegan, gluten-free) (leave blank for none): ")
        time = input("How much time do you have? (e.g., 15 min, 30 min, 1 hour): ")
        skill = input("What is your cooking skill level? (beginner, intermediate, expert): ")

        return ingredients, restrictions, time, skill

    # --- Execution Phase ---
    ingredients, restrictions, time, skill = get_recipe_inputs()

    # Create the prompt for the AI
    prompt = create_recipe_prompt(ingredients, restrictions, time, skill)

    print("\n🔄 Generating your recipes... Please wait a moment.")

    # Generate the recipe
    ai_response = generate_recipe(prompt)

    # Format and display the recipe
    format_recipe(ai_response)
