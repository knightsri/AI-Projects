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

def get_menu_choice(prompt, options):
    """Displays a menu and gets a valid choice from the user."""
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_yes_no(prompt):
    """Gets a yes or no answer from the user."""
    while True:
        choice = input(f"\n{prompt} (yes/no): ").lower().strip()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def get_recipe_inputs():
    """
    Gathers all necessary inputs from the user using menus.
    """
    print("🌿 Welcome! 🌿")
    print("Let's create a delicious recipe with the ingredients you have.\n")

    ingredients_input = input("Enter your available ingredients (comma-separated): ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',') if ingredient.strip()]

    # Dietary choices menu
    dietary_options = ["Non-Vegetarian", "Vegetarian", "Vegan", "Gluten-Free", "No specific restrictions"]
    restrictions = get_menu_choice("Select your dietary preference:", dietary_options)

    # Time choices menu
    time_options = ["15 minutes", "30 minutes", "1 hour", "More than 1 hour"]
    time = get_menu_choice("How much time do you have?", time_options)

    # Skill level menu
    skill_options = ["Beginner", "Intermediate", "Expert"]
    skill = get_menu_choice("What is your cooking skill level?", skill_options)

    # Healthy option
    healthy = get_yes_no("Would you like a healthy version of the recipe?")

    return ingredients, restrictions, time, skill, healthy

def check_basic_ingredients(ai_response):
    """
    Parses the recipe to find basic staples and confirms with the user.
    Returns True if the user has the ingredients, False otherwise.
    """
    # A list of common pantry staples to check for.
    basic_staples = ['salt', 'pepper', 'water', 'oil', 'sugar', 'flour', 'butter', 'garlic powder', 'onion powder', 'soy sauce', 'vinegar']
    required_staples = set()
    
    in_ingredients_section = False
    for line in ai_response.split('\n'):
        line_lower = line.lower().strip()
        # Heuristic to detect the start and end of ingredient lists
        if line_lower.startswith('### ingredients'):
            in_ingredients_section = True
            continue
        if line_lower.startswith('### instructions'):
            in_ingredients_section = False
            continue
            
        if in_ingredients_section:
            for staple in basic_staples:
                if staple in line_lower:
                    required_staples.add(staple.capitalize())

    if not required_staples:
        return True # No basic staples were found, so we can proceed.

    print("\nThe generated recipes require the following basic ingredients:")
    for staple in sorted(list(required_staples)):
        print(f"  - {staple}")
        
    have_staples = get_yes_no("Do you have these on hand?")
    
    if have_staples:
        return True
    else:
        print("\nPlease arrange these basic ingredients to make the recipes.")
        return False

# --- Main Application Logic ---
if __name__ == "__main__":
    print("--- Initializing Recipe-Remix-Chef ---\n")

    # --- Execution Phase ---
    ingredients, restrictions, time, skill, healthy = get_recipe_inputs()

    # Create the prompt for the AI
    prompt = create_recipe_prompt(ingredients, restrictions, time, skill, healthy)

    print("\n🔄 Generating your recipes... Please wait a moment.")

    # Generate the recipe
    ai_response = generate_recipe(prompt)
    
    # Before showing the recipe, check if the user has the basic ingredients
    if check_basic_ingredients(ai_response):
        # Format and display the recipe
        format_recipe(ai_response)