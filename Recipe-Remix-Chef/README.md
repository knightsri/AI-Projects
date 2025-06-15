# Recipe-Remix-Chef 🍳

**Recipe-Remix-Chef** is your personal kitchen assistant, designed to spark culinary creativity by generating unique recipes—including meat, vegetarian, and vegan options—using the ingredients you already have. Say goodbye to dinner dilemmas and hello to delicious, home-cooked meals tailored to your tastes and skills.

---

## 🚀 Getting Started: The Easiest Way

This project includes an automatic setup script to make getting started simple.

### **Step 1: Get the Code**

First, get the project files onto your computer.

1.  **Clone the Repository:**
    Open your terminal and run the following command:
    ```bash
    git clone https://github.com/knightsri/AI-Projects.git
    ```

2.  **Navigate to the Project Folder:**
    ```bash
    cd AI-Projects/Recipe-Remix-Chef
    ```
    *(Note: The final folder name might be different in your repository)*

### **Step 2: Get Your Google AI API Key**

This project uses the Google AI API, which requires a free API key.

1.  **Go to Google AI Studio:** [**Click here to create your API key**](https://aistudio.google.com/app/apikey)
2.  Click `Create API key in new project`.
3.  **Copy the key.** It's a long string of letters and numbers. You will need to paste this during the setup in the next step.

### **Step 3: Run the One-Time Setup**

This script will create a virtual environment, install packages, and ask for the API key you just created.

* **On macOS / Linux:**
    ```bash
    python3 install.py
    ```

* **On Windows:**
    ```bash
    python install.py
    ```
    Follow the on-screen instructions, and paste your API key when prompted.

### **Step 4: Run the App!**

To run the recipe generator, you must first activate the environment that the setup script created.

1.  **Activate the Environment:**
    * **On macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *You'll know it worked when you see `(venv)` at the beginning of your terminal prompt.*

2.  **Run the Main Application:**
    Once the environment is active, run the program:
    ```bash
    python main.py
    ```
    On subsequent runs, you just need to repeat this step (activate environment, then run `python main.py`).