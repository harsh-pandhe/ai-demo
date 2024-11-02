from openai import OpenAI
import secret

client = OpenAI(api_key=secret.OPENAI_API_KEY)


response = client.images.generate(
    model="dall-e-3",
    prompt="Krishna giving Arjuna the Gita on the battlefield of Kurukshetra",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)
