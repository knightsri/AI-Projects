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

## 🧩 **Core Components**

### **1. Input Processing (`main.py`)**

The `get_recipe_inputs()` function is responsible for gathering all the necessary details from the user via the command line.

* **Ingredients**: Accepts a comma-separated string and converts it into a list of ingredients.
* **Dietary Needs**: Prompts for dietary restrictions to ensure the recipe is suitable.
* **Time and Skill**: Takes into account the user's available time and cooking experience to tailor the recipe's complexity.

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
