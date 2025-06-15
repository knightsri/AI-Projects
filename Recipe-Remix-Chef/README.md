# Recipe-Remix-Chef: Complete Project Files

This document contains all the necessary files for the Recipe-Remix-Chef project. You can copy the code from each section and save it as the specified filename.

---

## 1. `README.md` (Updated)

This version directs users to the new, simplified setup script.

```markdown
# Recipe-Remix-Chef 🍳

**Recipe-Remix-Chef** is your personal kitchen assistant, designed to spark culinary creativity by generating unique recipes—including meat, vegetarian, and vegan options—using the ingredients you already have. Say goodbye to dinner dilemmas and hello to delicious, home-cooked meals tailored to your tastes and skills.

---

## 🚀 Getting Started: The Easiest Way

This project includes an automatic setup script to make getting started simple, even for non-technical users.

### **Step 1: Get the Code**

First, get the project files onto your computer.

* **Clone with Git:**
    ```bash
    git clone https://github.com/knightsri/AI-Projects.git
    ```
* **Navigate to the project folder:**
    ```bash
    cd AI-Projects/Recipe-Remix-Chef
    ```
    *(Note: The final folder name might be different in your repository)*

### **Step 2: Run the One-Time Setup**

This is the only setup you need to do. This script will create a virtual environment, install the necessary packages, and ask for your API key.

* **On macOS / Linux:**
    ```bash
    python3 install.py
    ```
* **On Windows:**
    ```bash
    python install.py
    ```
Follow the on-screen instructions. Once the setup is complete, you're ready to use the app.

### **Step 3: Run the App!**

To run the recipe generator, you need to first activate the environment that the setup script created.

* **On macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```
* **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```

Once the environment is active (you'll see `(venv)` in your terminal), run the main application:

```bash
python main.py