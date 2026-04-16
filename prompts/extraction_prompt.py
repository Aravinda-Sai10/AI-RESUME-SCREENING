from langchain_core.prompts import PromptTemplate
extraction_prompt = PromptTemplate.from_template("""
You are an AI recruiter.

Extract ONLY from the resume:
- Skills
- Experience (years + domain)
- Tools/Technologies

Resume:
{resume}

Rules:
- Do NOT assume anything
- Do NOT add skills not mentioned
- Output in structured format
""")