from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
client = OpenAI()

# Read CSV file
df = pd.read_csv(r"C:\Users\samyj\VsCode\AI_Training_01\project_3-AI_Research_Assistant\user_behavior_dataset.csv")

def analyze_data(df):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":f"You are a reseach assistant. Provide key insights from {df} only from demographics in point form"}],
        max_tokens=500,
        temperature=0.2
    )

    return response.choices[0].message.content

print(analyze_data(df))