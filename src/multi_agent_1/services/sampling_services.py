from crewai import Crew,Process
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg
from multi_agent_1.agents.sampling_agent import sampling_agent
from multi_agent_1.tasks.sampling_task import sampling_task

def generate_sampling_plan(
    topic:str,
    research_problem:str,
    research_question:str,
    research_design:str,
)->str:
 
 sampling_crew=Crew(
    agents=[sampling_agent],
    tasks=[sampling_task],
    process=Process.sequential,
    verbose=True
 )

 result=sampling_crew.kickoff(
    inputs={
        "topic":topic,
        "research_problem":research_problem,
        "research_question":research_question,
        "research_design":research_design,
    }
 )
 
 return str(result)