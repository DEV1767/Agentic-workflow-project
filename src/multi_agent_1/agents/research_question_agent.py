from sqlalchemy.sql.functions import mode
import os
from dotenv import load_dotenv
from crewai import Agent,LLM
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg


load_dotenv()

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
)

research_question_agent=Agent(
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
    allow_delegation=False
)