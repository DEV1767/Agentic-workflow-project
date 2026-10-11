from langgraph.graph import StateGraph,START,END

from multi_agent_1.state import ResearchState

from multi_agent_1.nodes import(
    research_problem_node,
    literature_review_node,
    research_question_node,
    research_design_node,
    sampling_node,
    data_analysis_node,
    research_writer_node
)

builder=StateGraph(ResearchState)

builder.add_node("research_problem",research_problem_node)
builder.add_node("literature_review",literature_review_node)
builder.add_node("research_question",research_question_node)
builder.add_node("research_design",research_design_node)
builder.add_node("sampling",sampling_node)
builder.add_node("data_analysis",data_analysis_node)
builder.add_node("research_writer",research_writer_node)


builder.add_edge(START,"research_problem")


builder.add_edge("research_problem","literature_review")
builder.add_edge("literature_review","research_question")
builder.add_edge("research_question","research_design")
builder.add_edge("research_design","sampling")
builder.add_edge("sampling","data_analysis")
builder.add_edge("data_analysis","research_writer")


builder.add_edge("research_writer",END)

research_graph=builder.compile()

