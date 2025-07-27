from dotenv import load_dotenv
import os

load_dotenv()

LLM_API_KEY = os.environ.get("GEMINI_API_KEY")
LLM_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
