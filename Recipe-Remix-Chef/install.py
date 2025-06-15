import os
import sys
import subprocess
import venv

def create_virtual_environment():
    """Creates a virtual environment named 'venv' if it doesn't exist."""
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        venv.create('venv', with_pip=True)
        print("Virtual environment 'venv' created.")
    else:
        print("Virtual environment 'venv' already exists.")

def install_dependencies():
    """Installs dependencies from requirements.txt into the virtual environment."""
    print("\nInstalling dependencies...")
    
    if sys.platform == "win32":
        pip_executable = os.path.join('venv', 'Scripts', 'pip.exe')
    else:
        pip_executable = os.path.join('venv', 'bin', 'pip')
    
    if not os.path.exists('requirements.txt'):
        print("Error: requirements.txt not found. Cannot install dependencies.")
        return False
        
    try:
        subprocess.check_call([pip_executable, 'install', '-r', 'requirements.txt'])
        print("\nDependencies installed successfully!")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nAn error occurred while installing dependencies.")
        return False

def prompt_for_api_key():
    """Prompts the user for their API key and saves it to a .env file."""
    print("\nConfiguring API Key...")
    env_file = '.env'
    
    api_key = input("Please paste your Google AI API key here and press Enter: ").strip()
    
    if not api_key:
        print("No API key provided. Setup cannot continue.")
        return False
        
    try:
        with open(env_file, 'w') as f:
            f.write(f'GOOGLE_API_KEY="{api_key}"\n')
        print(f"API key successfully saved to {env_file}")
        return True
    except IOError as e:
        print(f"Error: Could not write to {env_file}. {e}")
        return False

def main():
    """Main function to run the setup process."""
    print("--- Starting Project Setup ---")
    
    create_virtual_environment()
    
    if install_dependencies() and prompt_for_api_key():
        print("\n---------------------------------------------------------")
        print("✅ Setup complete!")
        print("To run the application, please activate the virtual environment:")
        if sys.platform == "win32":
            print("   On Windows, run: .\\venv\\Scripts\\activate")
        else:
            print("   On macOS/Linux, run: source venv/bin/activate")
        print("\nThen, run the main program with:")
        print("   python main.py")
        print("---------------------------------------------------------")
    else:
        print("\n---------------------------------------------------------")
        print("❌ Setup failed. Please review the errors above.")
        print("---------------------------------------------------------")

if __name__ == "__main__":
    main()
