import anthropic

client = anthropic.Anthropic(
    api_key="........"  # Replace with your actual API key
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
