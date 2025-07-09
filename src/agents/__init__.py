from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

llm = init_chat_model("anthropic:claude-3-5-sonnet-latest")
