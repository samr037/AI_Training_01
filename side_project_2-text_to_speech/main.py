from openai import OpenAI
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()
client = OpenAI()

# Prompt
prompt = ("Tell me a story about a brave knight that loves basketball")

# Function that will handle our text to speech
def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("tts_example.mp3")
    os.system("afplay tts_example.mp3")


# Function that will generate tour text
def generate_text(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.8,
        max_tokens=150
    )

    return response.choices[0].message.content

# Create a function that brings it all together

def gen_and_speak(prompt):
    text=generate_text(prompt)
    print("Generated text: '\n'", text)
    text_to_speech(text)

print(gen_and_speak(prompt))