from langchain_core.runnables import RunnableParallel, RunnableLambda

from multi_agent_1.tools.openalex_search import search_openalex
from multi_agent_1.tools.web_search import web_search_ddgs
from multi_agent_1.tools.tavily_search import web_search_tavily
from multi_agent_1.tools.duplicate_result import duplicate_result

# Search all sources in parallel
parallel_search = RunnableParallel(
    openalex=RunnableLambda(
        lambda x: search_openalex(x["query"], max_results=2)
    ),
    duckduckgo=RunnableLambda(
        lambda x: web_search_ddgs(x["query"])
    ),
    tavily=RunnableLambda(
        lambda x:web_search_tavily(x["query"])
    ),
)


# Run searches and remove duplicates
def search_and_deduplicate(query: str) -> list[dict]:
    results = parallel_search.invoke({"query": query})

    unique_results = duplicate_result(results)

    return unique_results