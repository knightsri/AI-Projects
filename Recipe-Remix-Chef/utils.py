import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def format_recipe(ai_response):
    """
    Parses the AI response and formats it with colors for better readability.
    """
    if not ai_response or ai_response.isspace():
        print(Fore.RED + "Sorry, I couldn't generate a recipe with those constraints. Please try different ingredients.")
        return

    print("\n" + Fore.CYAN + Style.BRIGHT + "="*50)
    print(Fore.CYAN + Style.BRIGHT + "      Your Custom Recipes! 🍳")
    print(Fore.CYAN + Style.BRIGHT + "="*50 + "\n")

    if ai_response.startswith("An error occurred"):
        print(Fore.RED + ai_response)
        return

    recipes = ai_response.split('\n---\n')

    for i, recipe_text in enumerate(recipes):
        if not recipe_text.strip():
            continue
        
        print(f"{Fore.MAGENTA}{Style.BRIGHT}--- RECIPE {i+1} ---\n")

        # Use a more robust way to handle sections
        sections = recipe_text.split('### ')
        for section in sections:
            if not section.strip():
                continue

            try:
                title, content = section.split('\n', 1)
                print(f"{Fore.YELLOW}{Style.BRIGHT}### {title.strip()}")
                print(content.strip() + "\n")
            except ValueError:
                # This handles the case where a section might just be a title
                print(f"{Fore.YELLOW}{Style.BRIGHT}### {section.strip()}\n")
