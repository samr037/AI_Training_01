from openai import OpenAI
from dotenv import load_dotenv
import base64


load_dotenv()
client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
# Path to your image
image_path = r"project_6-Image_caption\vlcsnap-2021-04-11-17h37m37s619.png"

# Getting the Base64 string
base64_image = encode_image(image_path)


# Image url
image_url = "https://kasm.iostack.fr/img/logo.svg"

# Function that can generate captions
def generate_captions(image_url):
    response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": [
                { "type": "input_text", "text": "what's in this image? If it's a car, try to identify brand and model" },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
)
    return response.output_text

# Print it out
print(generate_captions(image_url))
