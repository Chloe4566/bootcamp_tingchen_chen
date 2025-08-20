import os
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file"""
    load_dotenv()

def get_key(key: str):
    """Get a value from environment variables"""
    return os.getenv(key)

if __name__ == "__main__":
    load_env()
    print("API_KEY:", get_key("API_KEY"))
