from dotenv import load_dotenv
import os

load_dotenv('.env')

API_KEY: str = os.getenv('API')