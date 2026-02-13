import requests
import json
print("...Starting up ......")
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "google/gemma-3-4b-it:free",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            }
          }
        ]
      }
    ]
  })
)
print(" 1 -.response.json () ===================================================")
print(response.json())
print(" 2 -.response ===================================================")
print(response)
print(" 3 -.response.choices[0].message.content===================================================")
print(response.json().choices[0].message.content)
