from multi_agent_1.services.research_chain import research

question = "What are the latest developments in multi-agent AI?"

answer = research(question)

print("\n========== RESEARCH REPORT ==========\n")
print(answer)