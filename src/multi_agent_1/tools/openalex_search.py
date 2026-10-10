import os
import requests
from dotenv import load_dotenv

load_dotenv()


def search_openalex(query: str, max_results: int = 2) -> list[dict]:
    """Search OpenAlex for academic research papers."""

    url = "https://api.openalex.org/works"

    params = {
    "search": query.replace("?", "").replace("*", ""),
    "per_page": max_results,
}

    api_key = os.getenv("OPENALEX_API_KEY")

    if api_key:
        params["api_key"] = api_key

    try:
        response = requests.get(url, params=params, timeout=30)

        if not response.ok:
            print("OpenAlex status:", response.status_code)
            print("OpenAlex error:", response.text[:1000])
            response.raise_for_status()

        papers = response.json().get("results", [])

        return [
            {
                "title": paper.get("title"),
                "year": paper.get("publication_year"),
                "citations": paper.get("cited_by_count"),
                "doi": paper.get("doi"),
                "url": paper.get("id"),
                "abstract": paper.get("abstract_inverted_index"),
                "source": "OpenAlex",
            }
            for paper in papers
        ]

    except requests.RequestException as error:
        print(f"OpenAlex request failed: {error}")
        return []