from crewai import Agent
from multi_agent_1.config.llm import llm_1

research_writer_agent=Agent(
    role="Acedemic Research Report Writer",
    
    goal=(
        "Combine output from the research workflow into a "
        "Structured, coherent, evidence-based research report."
    ),

    backstory=(
        "You are an academic research writer experienced in "
        "organizing  research problems literature reviews,"
        "research question,  methodology, sampling, and analysis"
        "into clear academic reports. You never invent sources," 
        "data, statistical result, or research findings."
    ),
    llm=llm_1,
    verbose=True,
    allow_delegation=False
)


