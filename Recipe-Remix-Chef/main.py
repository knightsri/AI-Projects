from recipe_generator import create_recipe_prompt, generate_recipe
from utils import format_recipe

def get_recipe_inputs():
    """
    Gathers all necessary inputs from the user.
    """
    print("🌿 Welcome to the Recipe-Remix-Chef! 🌿")
    print("Let's create a delicious recipe with the ingredients you have.\n")

    ingredients_input = input("Enter your available ingredients (comma-separated): ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]

    restrictions = input("Any dietary restrictions? (e.g., vegan, vegetarian, gluten-free): ")
    time = input("How much time do you have? (e.g., 15 min, 30 min, 1 hour): ")
    skill = input("What is your cooking skill level? (beginner, intermediate, expert): ")

    return ingredients, restrictions, time, skill

if __name__ == "__main__":
    ingredients, restrictions, time, skill = get_recipe_inputs()

    # Create the prompt for the AI
    prompt = create_recipe_prompt(ingredients, restrictions, time, skill)

    print("\n🔄 Generating your recipe... Please wait a moment.")

    # Generate the recipe
    ai_response = generate_recipe(prompt)

    # Format and display the recipe
    format_recipe(ai_response)
