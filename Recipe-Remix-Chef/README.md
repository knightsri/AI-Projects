Recipe-Remix-Chef 🍳
Recipe-Remix-Chef is your personal kitchen assistant, designed to spark culinary creativity by generating unique recipes—including meat, vegetarian, and vegan options—using the ingredients you already have. Say goodbye to dinner dilemmas and hello to delicious, home-cooked meals tailored to your tastes and skills.

🚀 Getting Started: The Easiest Way
This project includes an automatic setup script to make getting started simple, even for non-technical users.

Step 1: Get the Code

First, get the project files onto your computer.

Clone with Git:

git clone [https://github.com/knightsri/AI-Projects.git](https://github.com/knightsri/AI-Projects.git)

Navigate to the project folder:

cd AI-Projects/Recipe-Remix-Chef

(Note: The final folder name might be different in your repository)

Step 2: Get Your Google AI API Key

This project uses the Google AI API, which requires a free API key.

Go to Google AI Studio: Click here to create your API key

Click Create API key in new project.

Copy the key. It's a long string of letters and numbers. You will need to paste this during the setup in the next step.

Step 3: Run the One-Time Setup

This script will create a virtual environment, install packages, and ask for the API key you just created.

On macOS / Linux:

python3 install.py

On Windows:

python install.py

Follow the on-screen instructions, and paste your API key when prompted.

Step 4: Run the App!

To run the recipe generator, you need to first activate the environment that the setup script created.

On macOS / Linux:

source venv/bin/activate

On Windows:

.\venv\Scripts\activate

Once the environment is active (you'll see (venv) in your terminal), run the main application:

python main.py

