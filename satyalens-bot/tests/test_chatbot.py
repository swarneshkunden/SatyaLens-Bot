import sys
import os
from dotenv import load_dotenv

# Add project root to sys.path to import src modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.chatbot import SatyaLensBot

# Load environment variables from .env file
load_dotenv()

# Config dictionary based on your .env variables
config = {
    'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
    'GOOGLE_SAFE_BROWSING_API_KEY': os.getenv('GOOGLE_SAFE_BROWSING_API_KEY'),
    'ARYA_AI_API_KEY': os.getenv('ARYA_AI_API_KEY'),
    'URLVOID_API_KEY': os.getenv('URLVOID_API_KEY'),
    'VIRUSTOTAL_API_KEY': os.getenv('VIRUSTOTAL_API_KEY')
}

# Instantiate your chatbot
bot = SatyaLensBot(config)

# List of test messages
test_messages = [
    "Check this site: https://example.com",
    "Is https://bit.ly/12345 safe?",
    "No URL, just a hello.",
    "Can you help me stay safe online?"
]

# Loop through and test responses
for msg in test_messages:
    print(f"User: {msg}")
    response = bot.process_message("test_user", "test_console", msg)
    print(f"Bot: {response}\n")

# This script tests the chatbot's URL extraction and analysis functionality.
# If this runs without errors, your chatbot is functioning correctly.
# Ensure to run this script in an environment where the necessary API keys are set in .env file.