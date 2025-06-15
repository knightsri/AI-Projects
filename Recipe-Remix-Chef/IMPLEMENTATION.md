# Recipe-Remix-Chef: Implementation Details

This document provides a technical overview of the **Recipe-Remix-Chef** project, detailing its current architecture, core components, and the logic behind its functionality. This version focuses on a robust, intelligent, terminal-based experience.

---
## **🏛️ Project Architecture**

The project's architecture is focused on a smart, interactive command-line workflow.

* **`install.py`**: A dedicated setup script that prepares the project environment. It creates a virtual environment, installs all required packages, and securely prompts for and saves the user's API key.

* **`main.py`**: The central orchestrator of the application. It manages the entire user input flow, including the new ingredient validation and cuisine-specific pantry checks. It then triggers recipe generation and sends the result to be formatted in the terminal.

* **`recipe_generator.py`**: This module is responsible for communicating with the Google AI text model. It constructs a highly detailed prompt that now includes context about the user's available spices and herbs.

* **`utils.py`**: This utility module is responsible for formatting the text-only recipe output with colors for display in the terminal.

* **`config.py`**, **`requirements.txt`**, **`.env`**: Standard configuration and dependency files. `requests` is no longer a dependency.

---
## **🧩 Core Components**

### **1. Intelligent User Input (`main.py`)**

The user interaction has been significantly enhanced to be more intelligent and prevent logical errors.

* **Symmetrical Ingredient Validation**: The `validate_ingredients` function now performs robust checks for both vegetarian and non-vegetarian selections.
    * If a user selects **Vegetarian/Vegan** but provides non-veg items, it warns them and allows them to correct the list.
    * If a user selects **Non-Vegetarian** but provides only vegetarian items, it displays examples of non-veg ingredients and prompts the user to add one, ensuring the request is logical.

* **Cuisine-Specific Pantry Check**: After a cuisine is selected, a `check_specialty_ingredients` function is called. This function uses a predefined map to ask the user if they have common herbs or spices for that cuisine (e.g., "Do you have common Italian herbs like oregano, basil, and rosemary?"). This "yes" or "no" answer is then passed to the AI to generate a more accurate recipe.

* **Expanded Choices & Streamlined Input**: The number of cuisine choices has been expanded to 10. All yes/no prompts now accept a single `y` or `n` for faster interaction. All prompts are color-coded for clarity.

### **2. Dynamic Prompt Engineering (`recipe_generator.py`)**

The prompt sent to the AI is now more context-aware and detailed:

* **Pantry Context**: The prompt now includes a new section, "Pantry Notes," which explicitly tells the AI whether the user has the relevant specialty spices for their chosen cuisine. This allows the AI to create a more authentic recipe.

* **Strict Ingredient Adherence**: The prompt continues to enforce the rule that the AI can **only** use the ingredients provided by the user, plus a short list of basic staples (salt, pepper, oil, water), preventing unexpected additions.

* **Nutritional Information Request**: The prompt mandates that the AI return an estimated nutritional breakdown for each recipe.

### **3. Terminal-First Output (`utils.py`)**

The focus is on providing a clean and readable terminal output:

* The `format_recipe` function in `utils.py` parses the AI's response, which contains two recipes separated by `---`.
* It uses the `colorama` library to print each section with distinct colors (e.g., magenta headers, yellow section titles), making the final output easy to read and visually organized.
