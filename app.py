from openai import OpenAI
import secret

client = OpenAI(api_key=secret.OPENAI_API_KEY)
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://www.smartsheet.com/sites/default/files/2021-11/IC-Construction-Billing-Invoice-Example-Template.png",
                    },
                },
            ],
        }
    ],
)

print(completion.choices[0].message.content)
