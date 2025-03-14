from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content = "Hello! You are a helpfull asistant."),
    HumanMessage(content = "I need help."),
    AIMessage()
]