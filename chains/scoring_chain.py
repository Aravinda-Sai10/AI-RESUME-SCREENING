from langchain_groq import ChatGroq
from prompts.scoring_prompt import scoring_prompt
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def run_scoring(match_result):
    chain = scoring_prompt | llm
    return chain.invoke({
        "match_result": match_result.content
    })