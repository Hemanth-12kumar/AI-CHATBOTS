
import ollama

print("===== AI CHATBOT =====")

while True:
    question = input("Enter a question:")

    if question.lower() == "exit"or"Bye":
        print("Chatbot: Goodbye!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\nChatbot:", response["message"]["content"])
