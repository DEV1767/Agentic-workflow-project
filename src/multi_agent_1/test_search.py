from multi_agent_1.services.research_question_services import generate_research_question

topic = "AI-based detection of fake job and internship offers"

research_problem = (
    "How can AI identify fraudulent job postings "
    "while minimizing false positives?"
)

literature_review = """
The available literature discusses NLP-based fake job detection
and multi-layer verification using text, company identity, and URL risk.
Only a small number of studies have been retrieved, so broader
research gaps remain unconfirmed.
"""

result = generate_research_question(
    topic=topic,
    research_problem=research_problem,
    literature_review=literature_review,
)

print("\n========== RESEARCH QUESTIONS ==========\n")
print(result)