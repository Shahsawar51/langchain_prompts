from langchain_core.prompts import PromptTemplate



# Refined Template for the chatbot
template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True,
    template="""
    Please summarize the research paper titled "{paper_input}".
    
    The explanation should be in a {style_input} style and should have a {length_input} length. 
    Focus on conveying the key concepts, methodologies, results, and conclusions of the paper.
    Use clear and precise language to match the selected style, ensuring the summary captures the essence of the research work.
    """
)

# save in json
template.save("template.json")