from langchain_core.prompts import PromptTemplate
explanation_prompt = PromptTemplate.from_template("""
Explain the score.

Match Result:
{match_result}

Score:
{score}

Return:
- Strengths
- Weaknesses
- Final justification

Keep it clear and logical.
""")