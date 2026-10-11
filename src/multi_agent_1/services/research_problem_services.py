from aiohttp.web_runner import GracefulExit
from crewai import Crew,Process
import crewai.llms.cache as crewai_cache
crewai_cache.mark_cache_breakpoint = lambda msg: msg
from multi_agent_1.agents.problem_agent import problem_agent
from multi_agent_1.tasks.problem_task import problem_task

def generate_research_problem(topic:str)->str:
    problem_crew=Crew(
        agents=[problem_agent],
        tasks=[problem_task],
        process=Process.sequential,
        verbose=True,
    )

    result=problem_crew.kickoff(
        inputs={"topic":topic}
    )

    return str(result)