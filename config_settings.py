import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Hugging Face API Key
HF_API_KEY = os.getenv("HF_API_KEY")

# AI Model Name
MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"

# Flask App Configurations
FLASK_DEBUG = True  # Set to False in production
