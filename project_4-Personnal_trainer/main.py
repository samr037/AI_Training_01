from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
client = OpenAI()

# Bring some fitness data
df = pd.read_csv(r"project_4-Personnal_trainer\Sleep_health_and_lifestyle_dataset.csv")
goals = []

# Create a way to add all of our fitness goals to a list

while True:
    goal = input("What are your health goals? Enter done once complete:")
    if goal.lower() == "done":
        break
    
    goals.append(goal)
# Pass these goals to the model
def trainer(goals, df):
    messages = []
    for goal in goals:
        messages.append({"role":"user","content":goal})
    messages.extend([
        {"role":"system","content":"Direct. Point form"},
        {"role":"assistant","content":f"You are a health expert. The person you are responding to is an accountant. Be technical an specific. reference this data {df} in your response."}
    ])

    response = client.chat.completions.create(
        model = "gpt-4",
        messages = messages,
        temperature = 0.8
    )

    return response.choices[0].message.content

# Call the model

print(trainer(goals,df))