import os
from tavily import TavilyClient
from dotenv import load_dotenv


load_dotenv()

api_key=os.getenv("TAVILY_API_KEY")


client=TavilyClient(api_key=api_key)


def web_search_tavily(query:str,max_result:int =3)->list[dict]:
    """Search the web and return relevent results using Tavily API."""
    
    responce=client.search(
        query=query,
        search_depth="basic",
        max_results=max_result,
    )

    results=[]

    for item in responce.get("results",[]):
        results.append(
            {
                "title":item.get("title",""),
                "url":item.get("url",""),
                "snippet":item.get("content",""),
                "source":"Tavily",
            }
        )
    return results