from celpy.evaluation import result
from multi_agent_1.graph import research_graph

def run_research(topic:str)->dict:
    """Run the complete research workflow."""

    initial_state={
        "topic":topic,
        "research_problem":"",
        "literature_review":"",
        "research_question":"",
        "research_design":"",
        "sampling_plan":"",
        "data_analysis":"",
        "final_report":"",
    }

    result=research_graph.invoke(initial_state)

    return result


if __name__=="__main__":

    topic=input("Enter your research topic:").strip()

    if not topic:
        print("Please enter a research topic.")
    else:
        result=run_research(topic)
        print("\n==========FINAL RESEARCH REPORT ==========\n")
        print(result["final_report"])

