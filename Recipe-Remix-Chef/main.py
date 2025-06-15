import os
import sys

try:
    from dotenv import load_dotenv
    from colorama import Fore, Style, init
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

# Initialize Colorama
init(autoreset=True)
load_dotenv()

# --- Data for Smart Checks ---
NON_VEG_KEYWORDS = [
    'beef', 'pork', 'lamb', 'goat', 'venison', 'chicken', 'duck', 'turkey', 
    'quail', 'sausage', 'ham', 'bacon', 'salami', 'fish', 'salmon', 'tuna', 
    'cod', 'shrimp', 'crab', 'lobster', 'mussel', 'oyster', 'squid', 
    'octopus', 'egg', 'eggs', 'anchovy', 'gelatin', 'lard'
]
SPECIALTY_INGREDIENTS = {
    "Indian": "common Indian spices (like cumin, coriander, turmeric, and garam masala)",
    "Italian": "common Italian herbs (like oregano, basil, and rosemary)",
    "Mexican": "common Mexican spices (like chili powder, cumin, and paprika)",
    "Chinese": "common Chinese sauces and spices (like soy sauce, ginger, and five-spice powder)",
    "Thai": "common Thai ingredients (like lemongrass, fish sauce, and curry paste)"
}

def get_menu_choice(prompt, options):
    """Displays a menu and gets a valid choice from the user."""
    print(Style.BRIGHT + Fore.GREEN + f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    
    while True:
        try:
            choice = int(input(Fore.YELLOW + "Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(Fore.RED + "Invalid choice. Please select a number from the list.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

def get_yes_no(prompt):
    """Gets a yes or no answer from the user."""
    while True:
        choice = input(Style.BRIGHT + Fore.GREEN + f"\n{prompt} (y/n): ").lower().strip()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print(Fore.RED + "Invalid input. Please enter 'y' or 'n'.")

def validate_ingredients(ingredients, dietary_choice):
    """Validates ingredients against dietary choice and handles conflicts."""
    is_veg_choice = dietary_choice in ["Vegetarian", "Vegan"]
    is_non_veg_choice = dietary_choice == "Non-Vegetarian"
    
    conflicting_items = [item for item in ingredients if item.lower() in NON_VEG_KEYWORDS]
    contains_non_veg = any(item.lower() in NON_VEG_KEYWORDS for item in ingredients)

    # Scenario 1: User chose a vegetarian diet but provided non-veg ingredients.
    if is_veg_choice and conflicting_items:
        print(Fore.RED + f"\nWarning: You selected a {dietary_choice} diet but provided non-vegetarian ingredients: {', '.join(conflicting_items)}.")
        retry = get_yes_no("Would you like to re-enter only vegetarian ingredients? If not, I will go ahead and create recipes with ingredient list provided by you.")
        if retry:
            new_ingredients_input = input("Please enter your vegetarian ingredients: ")
            return [ing.strip() for ing in new_ingredients_input.split(',') if ing.strip()]
        else:
            filtered_ingredients = [item for item in ingredients if item.lower() not in NON_VEG_KEYWORDS]
            print(Fore.YELLOW + f"Proceeding with only vegetarian ingredients: {', '.join(filtered_ingredients)}")
            return filtered_ingredients
            
    # Scenario 2: User chose a non-veg diet but provided only vegetarian ingredients.
    elif is_non_veg_choice and not contains_non_veg:
        print(Fore.RED + "\nWarning: You selected a Non-Vegetarian diet but did not provide any non-vegetarian ingredients.")
        print(Fore.CYAN + "Examples of non-veg items: chicken, beef, fish, shrimp, eggs, etc.")
        retry = get_yes_no("Would you like to add a non-vegetarian ingredient to your list?. If not, I will go ahead and create recipes with ingredient list provided by you.")
        if retry:
            new_ingredients_input = input("Please re-enter your full list of ingredients: ")
            return [ing.strip() for ing in new_ingredients_input.split(',') if ing.strip()]
            
    return ingredients

def check_specialty_ingredients(cuisine):
    """Asks the user if they have common spices/herbs for the selected cuisine."""
    if cuisine in SPECIALTY_INGREDIENTS:
        question = f"Do you have {SPECIALTY_INGREDIENTS[cuisine]}?"
        has_them = get_yes_no(question)
        if has_them:
            return f"The user has confirmed they have {SPECIALTY_INGREDIENTS[cuisine]}."
        else:
            return f"The user may not have {SPECIALTY_INGREDIENTS[cuisine]}. The recipe should be simple."
    return "No specific spice/herb information provided."


def get_recipe_inputs():
    """Gathers all necessary inputs from the user using menus."""
    print(Fore.CYAN + "🌿 Welcome! Let's create a delicious recipe with the ingredients you have. 🌿")

    ingredients_input = input(Style.BRIGHT + Fore.GREEN + "\nEnter your available ingredients (comma-separated): ")
    ingredients = [ing.strip() for ing in ingredients_input.split(',') if ing.strip()]

    cuisine_options = ["Any", "Indian", "Italian", "Mexican", "Chinese", "Thai", "Japanese", "Mediterranean", "French", "American"]
    cuisine = get_menu_choice("Select your preferred cuisine:", cuisine_options)
    
    specialty_info = check_specialty_ingredients(cuisine)

    dietary_options = ["Non-Vegetarian", "Vegetarian", "Vegan", "Gluten-Free", "No specific restrictions"]
    restrictions = get_menu_choice("Select your dietary preference:", dietary_options)
    
    ingredients = validate_ingredients(ingredients, restrictions)

    time_options = ["15 minutes", "30 minutes", "1 hour", "More than 1 hour"]
    time = get_menu_choice("How much time do you have?", time_options)

    skill_options = ["Beginner", "Intermediate", "Expert"]
    skill = get_menu_choice("What is your cooking skill level?", skill_options)

    healthy = get_yes_no("Would you like a healthy version of the recipe?")
    
    return ingredients, cuisine, restrictions, time, skill, healthy, specialty_info

if __name__ == "__main__":
    ingredients, cuisine, restrictions, time, skill, healthy, specialty_info = get_recipe_inputs()

    prompt = create_recipe_prompt(ingredients, cuisine, restrictions, time, skill, healthy, specialty_info)
    
    print(Fore.CYAN + "\n🔄 Generating your recipes... Please wait a moment.")
    ai_response = generate_recipe(prompt)

    if not ai_response or ai_response.startswith("An error occurred"):
        print(Fore.RED + f"\n❌ {ai_response}")
    else:
        format_recipe(ai_response)