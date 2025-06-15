from setuptools import setup, find_packages

setup(
    name="gai-lib",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "groq",
        "google-genai",
        "google-generativeai", 
        "openai==0.27.10",
        "requests",
        "python-dotenv",
        "langcodes"
    ],
    author="KnightSri",
    description="Multi-provider AI library for various projects",
    python_requires=">=3.7",
)
