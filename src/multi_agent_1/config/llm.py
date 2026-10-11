import os
from dotenv import load_dotenv
from crewai import LLM
import crewai.llms.cache as crewai_cache

load_dotenv()

crewai_cache.mark_cache_breakpoint = lambda msg: msg

# Model 1: gpt-oss-120b using primary Groq key
llm_1 = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
    max_tokens=3500,
)

# Model 2: gpt-oss-20b using secondary Groq key
llm_2 = LLM(
    model="groq/openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY_2"),
    temperature=0.2,
    max_tokens=3500,
)

# Default alias for backwards compatibility
llm = llm_1