from multi_agent_1.services.literature_services import conduct_literature_review

result = conduct_literature_review(
    topic="AI-based detection of fake job and internship offers",
    research_problem=(
        "How can AI identify fraudulent job postings "
        "while minimizing false positives?"
    ),
)

print("\n========== LITERATURE REVIEW ==========\n")
print(result)