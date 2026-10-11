from crewai import Crew,Process
import crewai.llms.cache as crewai_cache
crewai_cache.mark_cache_breakpoint = lambda msg: msg
from multi_agent_1.agents.researcher_writer_agent import research_writer_agent
from multi_agent_1.tasks.research_writer_task import research_writer_task


def generate_research_report(
    topic:str,
    research_problem:str,
    literature_review:str,
    research_question:str,
    research_design:str,
    sampling_plan:str,
    data_analysis:str,
)->str:
  writer_crew=Crew(
    agents=[research_writer_agent],
    tasks=[research_writer_task],
    process=Process.sequential,
    verbose=True,
  )

  result=writer_crew.kickoff(
    inputs={
         "topic": topic,
            "research_problem": research_problem,
            "literature_review": literature_review,
            "research_question": research_question,
            "research_design": research_design,
            "sampling_plan": sampling_plan,
            "data_analysis": data_analysis,
    }
  )

  return str(result)