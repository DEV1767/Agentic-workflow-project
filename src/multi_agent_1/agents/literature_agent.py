import os
from dotenv import load_dotenv
from crewai import Agent,LLM

load_dotenv()

llm=LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
)

literature_agent=Agent(
    role="Academic Literature Review Specialist",

    goal=(
        "Review existing academic research, summarize relevant findings, "
        "identify research gaps supported by evidence, and provide source URLs."
    ),
    backstory=(
        "You are an academic research specialist experienced in literature "
        "reviews, research paper analysis, and identifying research gaps. "
        "You distinguish verified findings from assumptions and never invent citations."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)