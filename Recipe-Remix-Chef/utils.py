def format_recipe(ai_response):
    """
    Formats the raw AI response for clean display.
    (This simple version just prints the response as is, but can be expanded)
    """
    # For this version, the prompt is structured enough that direct printing is clean.
    # Future enhancements could involve parsing into a dictionary or JSON object.
    print("\n" + "="*50)
    print("        Your Custom Recipe! 🍳")
    print("="*50 + "\n")
    print(ai_response)
    print("\n" + "="*50 + "\n")