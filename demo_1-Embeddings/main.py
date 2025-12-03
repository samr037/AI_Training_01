from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
client = OpenAI()

response = client.embeddings.create(
    input="Michael Jordan is better than Lebron James",
    model="text-embedding-3-large"
)

print(response.data[0].embedding)