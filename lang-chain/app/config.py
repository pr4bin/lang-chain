"""Centralized configuration management."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini AI Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")
