"""Centralized configuration management."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Perplexity AI Configuration
PPLX_API_KEY = os.getenv("PPLX_API_KEY")
PPLX_MODEL = os.getenv("PPLX_MODEL")
