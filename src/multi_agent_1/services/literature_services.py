from crewai import Crew, Process
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg
from multi_agent_1.agents.literature_agent import literature_agent
from multi_agent_1.tasks.literature_task import literature_task
from multi_agent_1.tools.parallel_search import search_and_deduplicate


def conduct_literature_review(
    topic: str,
    research_problem: str
) -> str:

    # Step 1: Search and remove duplicate results
    search_results = search_and_deduplicate(topic)

    # Step 2: Prepare evidence for the agent
    research_evidence = "\n\n".join(
        [
            f"Title: {paper.get('title', 'Unknown')}\n"
            f"Year: {paper.get('year', 'Unknown')}\n"
            f"Source: {paper.get('source', 'Unknown')}\n"
            f"URL: {paper.get('url', 'Unknown')}\n"
            f"Abstract: {paper.get('abstract', 'Not available')}"
            for paper in search_results
        ]
    )

    # Step 3: Run the Literature Review Agent
    literature_crew = Crew(
        agents=[literature_agent],
        tasks=[literature_task],
        process=Process.sequential,
        verbose=True,
    )

    result = literature_crew.kickoff(
        inputs={
            "topic": topic,
            "research_problem": research_problem,
            "search_results": research_evidence,
        }
    )

    return str(result)