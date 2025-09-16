import openai
import os

openai.api_key = os.getenv("Ssk-proj-JHhAmKwWt72IwLX3wul3mrnRz-vz_N4jH25WGz5Vo3KL9slWu27baBbB1qFC0sZMfkxbN8kxO8T3BlbkFJ_TKI8H4Jx6SvgcABOPeP3IRVKBVHE1RYvjn7us8ynKfySTKdKNNsqyoj9FRVONS0Ksyc_ffMMA")

def chat_with_gpt():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
                 v
        bot_reply = response['choices'][0]['message']['content']
        print("Chatbot:", bot_reply)
jn/!b
if __name__ ==a1wain__":
    chat_with_gpt()
