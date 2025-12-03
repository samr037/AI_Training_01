from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


# Audio file
audio_file = open(r"C:\Users\samyj\VsCode\AI_Training_01\Enregistrement.m4a", "rb")

# Transcription
transcribe = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

print(transcribe.text)
