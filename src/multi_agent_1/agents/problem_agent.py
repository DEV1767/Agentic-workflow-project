import os

from crewai import Agent, LLM
from dotenv import load_dotenv
import crewai.llms.cache as crewai_cache



crewai_cache.mark_cache_breakpoint = lambda msg: msg


load_dotenv()

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
)

problem_agent = Agent(
    role="Research Problem Identification Specialist",

    goal=(
        "Identify and clearly define the research problem, "
        "its scope, affected stakeholders, and potential research gaps."
    ),

    backstory=(
        "You are an experienced research analyst who helps researchers "
        "transform broad topics into clear, specific, and researchable problems."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False,
)