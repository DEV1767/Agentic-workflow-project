from botocore import model
import os
from dotenv import load_dotenv
from crewai import LLM
import crewai.llms.cache as crewai_cache

load_dotenv()

crewai_cache.mark_cache_breakpoint=lambda msg:msg

llm=LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)