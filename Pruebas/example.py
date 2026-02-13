from openai import OpenAI
print(".... pRIOR OPEN CLIENT ......")
OPENROUTER_API_KEY='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'



client = OpenAI()
print(".... Starting UP ......")
response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text) 