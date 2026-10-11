from crewai import Crew,Process
import crewai.llms.cache as crewai_cache
crewai_cache.mark_cache_breakpoint = lambda msg: msg
from multi_agent_1.agents.data_analysis_agent import data_analysis_agent
from multi_agent_1.tasks.data_analysis_task import data_analysis_task


def generate_data_analysis_plan(
    topic:str,
    research_problem:str,
    research_question:str,
    research_design:str,
    sampling_plan:str,
    dataset_information:str,
)->str:

 analysis_crew=Crew(
    agents=[data_analysis_agent],
    tasks=[data_analysis_task],
    process=Process.sequential,
    verbose=True,
 )

 result=analysis_crew.kickoff(
    inputs={
        "topic":topic,
        "research_problem":research_problem,
        "research_question":research_question,
        "research_design":research_design,
        "sampling_plan":sampling_plan,
        "dataset_information":dataset_information,
    }
 )

 return str(result)