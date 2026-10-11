from crewai import Crew,Process
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg
from multi_agent_1.agents.research_design_agent import research_design_agent
from multi_agent_1.tasks.research_design_task import research_design_task

def generate_research_design(
    topic:str,
    research_problem:str,
    literature_review:str,
    research_question:str,
)->str:

  research_design_crew=Crew(
    agents=[research_design_agent],
    tasks=[research_design_task],
    process=Process.sequential,
    verbose=True,
  )

  result=research_design_crew.kickoff(
    inputs={
        "topic":topic,
        "research_problem":research_problem,
        "literature_review":literature_review,
        "research_question":research_question,
    }
  )

  return str(result)