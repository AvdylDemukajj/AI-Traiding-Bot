# config.py
from dotenv import load_dotenv
import os

# Ngarkon variablat nga .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = os.getenv("BASE_URL")