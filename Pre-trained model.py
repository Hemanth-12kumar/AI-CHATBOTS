from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

response = chatbot(
    "chatbot is a  ",
    max_new_tokens=100
)
 
print(response)


