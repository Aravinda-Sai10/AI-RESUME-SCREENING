from langchain_core.prompts import PromptTemplate
matching_prompt = PromptTemplate.from_template("""
Compare resume with job description.

Job Description:
{jd}

Extracted Resume:
{extracted}

Return:
- Matching Skills
- Missing Skills
- Match Percentage (0-100)

Be strict and realistic.
""")