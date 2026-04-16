from langchain_groq import ChatGroq
from prompts.extraction_prompt import extraction_prompt
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)
def run_extraction(resume):
    chain = extraction_prompt | llm
    return chain.invoke({
        "resume": resume
    })