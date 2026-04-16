import os
from dotenv import load_dotenv

load_dotenv()

from chains.extraction_chain import run_extraction
from chains.matching_chain import run_matching
from chains.scoring_chain import run_scoring
from chains.explanation_chain import run_explanation


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

jd = read_file("data/job_description.txt")

resumes = {
    "Strong": "data/strong_resume.txt",
    "Average": "data/average_resume.txt",
    "Weak": "data/weak_resume.txt"
}

print("\n==============================================")
print(" AI RESUME SCREENING SYSTEM ")
print("==============================================")

for label, path in resumes.items():

    resume = read_file(path)

    # 🔥 Extract name from resume (FIRST LINE)
    name_line = resume.split("\n")[0]
    name = name_line.replace("Name:", "").strip()

    print("\n==============================================")
    print(f"Screening: {label} Candidate - {name}")
    print("==============================================")

    print("\n[Step 1] Extracting skills...")
    extracted = run_extraction(resume)
    print("✅ Skills extracted!")

    print("\n[Step 2] Matching requirements...")
    match = run_matching(jd, extracted)
    print("✅ Matches analyzed!")

    print("\n[Step 3] Calculating score...")
    score = run_scoring(match)
    print(f"✅ Score: {score.content}")

    print("\n[Step 4] Explaining...")
    explanation = run_explanation(match, score)
    print("✅ Explanation ready!")

    print("\nExplanation:")
    print(explanation.content)

print("\n==============================================")
print(" FINAL SCREENING COMPLETED ")
print("==============================================")