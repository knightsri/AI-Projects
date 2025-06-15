
# Recipe-Remix-Chef

**Recipe-Remix-Chef** is a fun Python project that acts as your personal kitchen assistant. It's designed to spark culinary creativity by generating unique vegan and vegetarian (egg-free) recipes using the ingredients you already have. Say goodbye to food waste and hello to delicious, home-cooked meals tailored to your tastes and skills. 🧑‍🍳

## 🎯 **Goal**

The primary goal of this project is to provide users with a smart and intuitive way to create recipes from a given set of ingredients. It aims to make cooking more accessible, reduce food waste, and encourage experimentation in the kitchen.

## ✨ **Core Features**

* **Ingredient-Based Recipes**: Generates recipes based on a user-provided list of ingredients.
* **Dietary Customization**: Caters to specific dietary needs, focusing on vegan and vegetarian (no egg) options.
* **Time & Skill Adaptable**: Suggests recipes that align with your available cooking time and level of expertise.
* **Smart Substitutions**: Offers intelligent suggestions for missing or alternative ingredients.
* **User-Friendly Interface**: Simple command-line interaction makes it easy to use.

## 🚀 **Getting Started**

### **Prerequisites**

* Python 3.7+
* Google AI API Key

### **Installation**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/knightsri/AI-Projects.git
    cd Recipe-Remix-Chef
    ```

2.  **Install the necessary packages:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    Create a file named `.env` in the root directory and add your Google AI API key as follows:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

### **How to Use**

Execute the main script from your terminal:

```bash
python main.py