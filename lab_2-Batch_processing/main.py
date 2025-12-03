from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# A list of prompts
prompts = [
    "Tell me a story about a warrior princess",
    "Generate a list of 5 business ideas",
    "Explain the theori of relativity in simple terms",
    "Write a poem about Michael Jordan"
]

# Function to process prompts
def process_prompts(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        max_tokens=250,
        temperature=0.8
    )

    return response.choices[0].message.content

results = []

for prompt in prompts:
    result = process_prompts(prompt)
    results.append(result)


for i, result in enumerate(results):
    print(f"Prompt {i+1}: {prompts[i]}")
    print(f"Response {i+1}: {result}")

