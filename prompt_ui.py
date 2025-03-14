import os
from dotenv import load_dotenv
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()
model = ChatOpenAI(model="gpt-4", temperature=1.5)

# Streamlit UI
st.header("OpenAI Chatbot For Langchain Prompts")

# User inputs
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need", 
        "BERT: Pre-training of Deep Bidirectional Transformers", 
        "GPT-3: Language Models are Few-Shot Learners", 
        "Diffusion Models Beat GANs on Image Synthesis", 
        "Another Research Paper"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly", 
        "Technical", 
        "Code-Oriented", 
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 lines)", 
        "Medium (5-8 lines)", 
        "Long (detailed explanation)"
    ]
)

# Refined Template for the chatbot
template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""
    Please summarize the research paper titled "{paper_input}".
    
    The explanation should be in a {style_input} style and should have a {length_input} length. 
    Focus on conveying the key concepts, methodologies, results, and conclusions of the paper.
    Use clear and precise language to match the selected style, ensuring the summary captures the essence of the research work.
    """
)


filled_template = template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=length_input
    )

# Handle button click
if st.button("Summarize"):
    try:
        result = model.invoke([HumanMessage(content=filled_template)])
        st.write(result.content)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Success message
st.success("LangChain Chatbot ready to summarize research papers! 🚀")

# Let me know if you want any more improvements! 🚀
