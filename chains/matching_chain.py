from langchain_groq import ChatGroq
from prompts.matching_prompt import matching_prompt
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)
def run_matching(jd, extracted):
    chain = matching_prompt | llm
    return chain.invoke({
        "jd": jd,
        "extracted": extracted.content
    })