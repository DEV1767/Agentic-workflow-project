import time
from multi_agent_1.state import ResearchState

from multi_agent_1.services.research_problem_services import generate_research_problem
from multi_agent_1.services.literature_services import conduct_literature_review
from multi_agent_1.services.research_question_services import generate_research_question
from multi_agent_1.services.research_design_services import generate_research_design
from multi_agent_1.services.sampling_services import generate_sampling_plan
from multi_agent_1.services.data_analysis_services import generate_data_analysis_plan
from multi_agent_1.services.research_writer_services import generate_research_report



def research_problem_node(state: ResearchState) -> dict:
    """Generate the research problem using CrewAI."""
    result = generate_research_problem(
        topic=state["topic"]
    )
    return {
        "research_problem": result
    }

def literature_review_node(state: ResearchState) -> dict:
    """Search research papers and generate a literature review."""
    time.sleep(3)  # Brief delay to replenish Groq TPM quota
    result = conduct_literature_review(
        topic=state["topic"],
        research_problem=state["research_problem"][:2500],
    )
    return {
        "literature_review": result,
    }

def research_question_node(state: ResearchState) -> dict:
    """Generate research questions and objectives."""
    time.sleep(3)
    result = generate_research_question(
        topic=state["topic"],
        research_problem=state["research_problem"][:2000],
        literature_review=state["literature_review"][:2500],
    )
    return {
        "research_question": result,
    }

def research_design_node(state: ResearchState) -> dict:
    """Generate the research design and hypotheses."""
    time.sleep(3)
    result = generate_research_design(
        topic=state["topic"],
        research_problem=state["research_problem"][:2000],
        literature_review=state["literature_review"][:2500],
        research_question=state["research_question"][:1500],
    )
    return {
        "research_design": result,
    }

def sampling_node(state: ResearchState) -> dict:
    """Generate the sampling plan."""
    time.sleep(3)
    result = generate_sampling_plan(
        topic=state["topic"],
        research_problem=state["research_problem"][:2000],
        research_question=state["research_question"][:1500],
        research_design=state["research_design"][:2000],
    )
    return {
        "sampling_plan": result,
    }

def data_analysis_node(state: ResearchState) -> dict:
    """Generate the data collection and analysis plan."""
    time.sleep(3)
    result = generate_data_analysis_plan(
        topic=state["topic"],
        research_problem=state["research_problem"][:2000],
        research_question=state["research_question"][:1500],
        research_design=state["research_design"][:2000],
        sampling_plan=state["sampling_plan"][:1500],
        dataset_information=(
            "No actual dataset has been provided yet. "
            "Prepare an analysis plan without inventing results."
        ),
    )
    return {
        "data_analysis": result,
    }

def research_writer_node(state: ResearchState) -> dict:
    """Generate the final research report."""
    time.sleep(3)
    result = generate_research_report(
        topic=state["topic"],
        research_problem=state["research_problem"][:2000],
        literature_review=state["literature_review"][:2500],
        research_question=state["research_question"][:1500],
        research_design=state["research_design"][:2000],
        sampling_plan=state["sampling_plan"][:1500],
        data_analysis=state["data_analysis"][:1500],
    )
    return {
        "final_report": result,
    }