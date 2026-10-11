from crewai import Agent
from multi_agent_1.config.llm import llm

problem_agent = Agent(
    role="Research Problem Identification Specialist",

    goal=(
        "Identify, define, and explain the research problem "
        "based on the research topic."
    ),

    backstory=(
        "You are an experienced research specialist who helps "
        "researchers identify meaningful problems, understand "
        "their significance, and define the scope of a study."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False,
)