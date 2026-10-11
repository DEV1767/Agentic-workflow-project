from crewai import Crew,Process
import crewai.llms.cache as crewai_cache
crewai_cache.mark_cache_breakpoint = lambda msg: msg
from multi_agent_1.agents.research_question_agent import research_question_agent
from multi_agent_1.tasks.research_question_task import research_question_task

def generate_research_question(
    topic:str,
    research_problem:str,
    literature_review:str,
)->str:
  crew=Crew(
    agents=[research_question_agent],
    tasks=[research_question_task],
    process=Process.sequential,
    verbose=True,
  )

  result=crew.kickoff(
    inputs={
        "topic":topic,
        "research_problem":research_problem,
        "literature_review":literature_review,

    }
  )

  return str(result)