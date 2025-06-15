# Recipe-Remix-Chef: Implementation Details

This document provides a technical overview of the **Recipe-Remix-Chef** project, detailing its architecture, core components, and the logic behind its functionality.

## 🏛️ **Project Architecture**

The project follows a modular structure to ensure clarity and maintainability:

* **`main.py`**: The entry point of the application. It orchestrates the flow from user input to recipe display.
* **`config.py`**: Handles the configuration, specifically loading the API key from environment variables.
* **`recipe_generator.py`**: Contains the logic for interacting with the Google AI model, including prompt creation and response generation.
* **`utils.py`**: A utility module for parsing and formatting the AI's raw output into a readable recipe format.
* **`requirements.txt`**: Lists all the Python dependencies required for the project.
* **`.env`**: Stores sensitive information like API keys.
* **`install.py`**:A dedicated setup script that prepares the project environment. 

## 🧩 **Core Components**

### **1. Input Processing (`main.py`)**

The user interaction has been significantly improved by replacing free-form text input with a numbered menu system:

get_menu_choice(): A reusable function that displays a list of options (e.g., for dietary needs, time, skill level) and validates that the user enters a valid number from the list.

get_yes_no(): A helper function to handle the "healthy version" preference, cleanly processing "yes" or "no" answers.

This approach minimizes user error, prevents typos, and makes the application faster and more intuitive to use.


### **2. Prompt Engineering (`recipe_generator.py`)**

The `create_recipe_prompt()` function is the heart of the recipe generation process. It crafts a detailed and structured prompt for the AI model.

* **Constraint-Based Strategy**: The prompt explicitly outlines the user's ingredients, dietary constraints, time limits, and skill level.
* **Structured Output Request**: It instructs the AI to provide the output in a specific format, including a recipe name, an ingredients list with quantities, step-by-step instructions, and cooking tips. This makes the response predictable and easy to parse.

### **3. AI Model Interaction (`recipe_generator.py`)**

The `generate_recipe()` function manages the communication with the Google Generative AI model.

* **API Integration**: It sends the engineered prompt to the AI model.
* **Error Handling**: Includes basic error handling to manage potential issues during the API call.

### **4. Output Processing (`utils.py`)**

The `format_recipe()` function takes the raw text response from the AI and transforms it into a structured, user-friendly format.

* **Parsing Logic**: It parses the AI's output to separate the recipe name, ingredients, instructions, and tips.
* **Shopping List**: (Optional) This function could be extended to identify ingredients the user doesn't have and compile a shopping list.

### **5. Automated Setup (install.py) **

To simplify the initial setup for non-technical users, a dedicated script handles all prerequisites:

Virtual Environment Creation: It automatically creates a venv folder to isolate the project's dependencies from the user's system Python, preventing conflicts.

Dependency Installation: It uses the subprocess module to call pip from within the newly created virtual environment, ensuring packages from requirements.txt are installed in the correct location.

API Key Configuration: It provides a clear command-line prompt for the user to enter their API key and writes it directly to the .env file, so the user only has to perform this sensitive step once.

## 🐍 **Python Implementation Snippets**

Here are some key functions that illustrate the project's logic:

**Prompt Creation (`recipe_generator.py`)**
```python
def create_recipe_prompt(ingredients, restrictions, time, skill):
    prompt = f"""
Create a creative and delicious recipe with the following constraints:
- **Primary Ingredients:** {', '.join(ingredients)}
- **Dietary Restrictions:** {restrictions} (strictly no egg)
- **Max Cooking Time:** {time}
- **Skill Level:** {skill}

Please provide the output with the following sections:
1.  **Recipe Name**
2.  **Ingredients List** (including quantities)
3.  **Step-by-Step Instructions**
4.  **Cooking Tips** for a {skill} cook.
5.  **Substitutions** for missing ingredients.
"""
    return prompt
