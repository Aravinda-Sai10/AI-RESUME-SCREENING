from langchain_groq import ChatGroq
from prompts.explanation_prompt import explanation_prompt
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)
def run_explanation(match_result, score):
    chain = explanation_prompt | llm
    return chain.invoke({
        "match_result": match_result.content,
        "score": score.content
    })