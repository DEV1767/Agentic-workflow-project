from langchain_core.runnables import RunnableParallel,RunnableLambda
from multi_agent_1.tools.openalex_search import search_openalex
from multi_agent_1.tools.web_search import web_search_ddgs
from multi_agent_1.tools.tavily_search import web_search_tavily

parallel_search=RunnableParallel(
    openalex=RunnableLambda(
        lambda x:search_openalex(x["query"])
    ),
    duckduckgo=RunnableLambda(
        lambda x:web_search_ddgs(x["query"])
    ),
    tavily=RunnableLambda(
        lambda x:web_search_tavily(x["query"])
    )
)
