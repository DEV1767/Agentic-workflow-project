from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from multi_agent_1.tools.parallel_search import parallel_search

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2,
)

prompt = ChatPromptTemplate.from_template("""
You are an AI Research Assistant.

Answer the user's question using the provided search results.

User question:
{query}

Search results:
{results}

Instructions:
1. Summarize the most relevant information.
2. Use academic papers and web sources where relevant.
3. Include source URLs when available.
4. Never invent facts or references.
5. If the search results are insufficient, explain the limitation.
""")

research_chain = prompt | llm | StrOutputParser()


def research(query: str) -> str:
    """Retrieve results from all three search providers."""

    results = parallel_search.invoke({"query": query})

    answer = research_chain.invoke({
        "query": query,
        "results": results,
    })

    return answer