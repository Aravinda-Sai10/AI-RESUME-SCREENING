from langchain_core.prompts import PromptTemplate

scoring_prompt = PromptTemplate.from_template("""
Based on the matching analysis:

{match_result}

Give a FINAL SCORE (0–100).

Rules:
- Strong match → 80–100
- Average → 50–79
- Weak → below 50
- Do NOT explain, only number
""")