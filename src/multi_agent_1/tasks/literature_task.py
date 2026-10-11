from crewai import Task
from multi_agent_1.agents.literature_agent import literature_agent

literature_task=Task(
    description=(
    "Conduct a literature review on: {topic}\n\n"
    "Research problem:\n{research_problem}\n\n"
    "Actual search results:\n{search_results}\n\n"
    "Tasks:\n"
    "1. Identify relevant previous studies.\n"
    "2. Summarize their methods and findings.\n"
    "3. Identify limitations in existing research.\n"
    "4. Identify potential research gaps supported by the evidence.\n"
    "5. Include source titles, years, and URLs when available.\n"
    "6. Distinguish verified findings from assumptions.\n"
    "Never invent papers, findings, or citations."
    ),
    expected_output=(
        "A structured literature review containing previous studies, "
        "methods, findings, limitations, evidence-supported research gaps, "
        "and source URLs."
    ),
    agent=literature_agent,
)