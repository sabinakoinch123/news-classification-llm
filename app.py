import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the secret key safely
load_dotenv()

# Initialize the OpenAI connection
client = OpenAI()

print("🤖 Interactive OpenAI Chatbot Initialized!")
print("Type your prompt below and press Enter. (Type 'quit' to exit)\n")

while True:
    user_prompt = input("You: ")
    
    if user_prompt.lower() == 'quit':
        print("Goodbye!")
        break
        
    if not user_prompt.strip():
        continue

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful and concise coding assistant."},
                {"role": "user", "content": user_prompt}
            ]
        )
        print(f"AI: {response.choices[0].message.content}\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")
        break
