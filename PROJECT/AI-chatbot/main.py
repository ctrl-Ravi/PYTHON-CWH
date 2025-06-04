import os
from openai import OpenAI

key = "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" 
messages = []

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=key,
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="deepseek/deepseek-chat-v3-0324:free"
    )

    response_message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(response_message)
    print(f"pelupa: {response_message['content']}")

if __name__ == "__main__":
    print("Pelupa: Hi I am pelupa, how may I help you?\n")
    while True:
        user_question = input()
        print(f"You: {user_question}")
        completion(user_question)
