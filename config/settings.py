import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
