from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def analyse_sentiment(text):
    prompt=f"Analyze the sentiment in a SINGLE WORD without dot or anything, of the following text: '{text}'"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"user","content":prompt}],
        max_tokens=50,
        temperature=0.3
    )
    print(f"Input: {text}")
    print(f"Sentiment: {response.choices[0].message.content}")


text = "The product works well, but support was so bad"
analyse_sentiment(text)