from crewai import Agent
from multi_agent_1.config.llm import llm

research_question_agent = Agent(
    role="Research Question and Objective specialist",
    goal=(
        "Develop clear, specific, measurable, and researchable questions "
        "and objectives based on the research problem and literature review."
    ),
    backstory=(
        "You are an experienced research methodologist. "
        "You convert research problems and literature reviews into "
        "focused research questions and measurable objectives. "
        "You never invent evidence or claim that assumptions are proven facts."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)