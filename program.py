import anthropic

client = anthropic.Anthropic(
    api_key="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"  # Replace with your actual API key
)

user_input = input("Enter your message: ")

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": user_input}
    ]
)

print(message.content)
