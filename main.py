import os
from dotenv import load_dotenv

load_dotenv()
print(f"Hello: {os.environ['OPENAI_APIKEY']}")