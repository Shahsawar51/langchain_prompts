from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

# Define the chat template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "Hello! I am a chatbot. You can start by asking me anything."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# Function to load chat history from a text file
def load_chat_history(file_path):
    chat_history = []
    with open(file_path, "r") as file:
        for line in file:
            role, content = line.strip().split(": ", 1)
            if role == "System":
                chat_history.append(SystemMessage(content=content))
            elif role == "Human":
                chat_history.append(HumanMessage(content=content))
            elif role == "AI":
                chat_history.append(AIMessage(content=content))
    return chat_history

# Load chat history from the text file
chat_history = load_chat_history("chat_history.txt")

# Initialize the ChatOpenAI model
model = ChatOpenAI(model="gpt-4", temperature=1.5)

# Create the prompt with the loaded chat history and invoke the model
result = model.invoke(chat_template.format(chat_history=chat_history, query="What is the summary of the conversation?"))

# Print the result
print(result.content)
