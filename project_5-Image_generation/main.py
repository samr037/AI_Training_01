from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# Function that can generate the visuals
def generate_picture():
    response = client.images.generate(
        model="dall-e-3",
        prompt="Programmer bluiding a robot dinosaur",
        size="1024x1024"
    )

    return response.data[0].url

image_url = generate_picture()

print("Generated image URL: ", image_url)
# Output