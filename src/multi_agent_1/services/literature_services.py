from crewai import Crew, Process
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg

from multi_agent_1.agents.literature_agent import literature_agent
from multi_agent_1.tasks.literature_task import literature_task
from multi_agent_1.tools.parallel_search import parallel_search


def conduct_literature_review(
    topic: str,
    research_problem: str,
) -> str:

    # Step 1: Search academic papers and web sources
    search_results = parallel_search.invoke({
        "query": topic
    })

    # Step 2: Prepare evidence for the agent
    research_evidence = str(search_results)

    # Step 3: Create the CrewAI crew
    literature_crew = Crew(
        agents=[literature_agent],
        tasks=[literature_task],
        process=Process.sequential,
        verbose=True,
    )

    # Step 4: Execute the literature review
    result = literature_crew.kickoff(
        inputs={
            "topic": topic,
            "research_problem": research_problem,
            "search_results": research_evidence,
        }
    )

    return str(result)