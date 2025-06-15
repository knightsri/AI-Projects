import colorama
from colorama import Fore, Style

# Initialize colorama to automatically reset styles after each print statement
colorama.init(autoreset=True)

def format_recipe(ai_response):
    """
    Parses the AI response and formats it with colors for better readability.
    """
    print("\n" + Fore.CYAN + "="*50)
    print(Fore.CYAN + "      Your Custom Recipes! 🍳")
    print(Fore.CYAN + "="*50 + "\n")

    # Check if an error message was returned instead of a recipe
    if ai_response.startswith("An error occurred"):
        print(Fore.RED + ai_response)
        return

    # Split the entire response into two recipes using the '---' separator
    recipes = ai_response.split('\n---\n')

    for i, recipe_text in enumerate(recipes):
        if not recipe_text.strip():
            continue
        
        # Print a header for each recipe
        print(f"{Fore.MAGENTA}{Style.BRIGHT}--- RECIPE {i+1} ---\n")

        # Split each recipe into its sections based on the '###' markdown headings
        sections = recipe_text.split('### ')
        for section in sections:
            # Skip any empty strings that result from splitting
            if not section.strip():
                continue

            # Split each section into a title and its content
            try:
                title, content = section.split('\n', 1)
            except ValueError:
                # Handle cases where a section might not have content
                title = section.strip()
                content = ""

            # Print the title in a bright, bold color and the content in the default color
            print(f"{Fore.YELLOW}{Style.BRIGHT}### {title.strip()}")
            print(content.strip() + "\n")
