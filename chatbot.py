from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the ChatOpenAI model
model = ChatOpenAI()

# Initialize chat history with a system message
chat_history = [
    SystemMessage(content="Hello! I am a chatbot. You can start by asking me anything.")
]

# Start an infinite loop to interact with the user
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print("AI: ", result.content)

# Save chat history to a text file
with open("chat_history.txt", "w") as file:
    for message in chat_history:
        if isinstance(message, SystemMessage):
            role = "System"
        elif isinstance(message, HumanMessage):
            role = "Human"
        elif isinstance(message, AIMessage):
            role = "AI"
        file.write(f"{role}: {message.content}\n")

print("Chat history saved to chat_history.txt")