from ddgs import results
import os
from tavily import TavilyClient
from ddgs import DDGS
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("TAVILY_API_KEY")


client=TavilyClient(api_key=api_key)

def web_search_ddgs(query:str,max_result:int=3)->list[dict]:
    
    """Perform web search and return relevent result."""

    try:
        with DDGS() as ddgs:
            results=list(
                ddgs.text(
                    query,
                    max_result=max_result
                )
            )
        return [
            {
                "title":result.get("title",""),
                "url":result.get("href",""),
                "snippet":result.get("body","")
            }
            for result in results
            
            ]
    except Exception as e :
        print(f"Search failed using DDGS: {e}")
        return []


