from crewai import Task
from multi_agent_1.agents.research_question_agent import research_question_agent

research_design_task=Task(
    description="""
    Develop a research design and formulate hypotheses for the study.

    Research Topic:
    {topic}

    Research Problem:
    {research_problem}

    Literature Review:
    {literature_review}

    Research Questions and Objectives:
    {research_questions}

    Complete the following sections:

    A. Research Approach
    - Explain whether a quantitative, qualitative, or mixed-methods
      approach is appropriate.
    - Explain why.

    B. Research Design
    - Recommend a suitable research design.
    - Explain how the research objectives will be addressed.

    C. Research Variables
    - Identify independent, dependent, and control variables
      where applicable.
    - If variables do not apply, explain why.

    D. Hypotheses
    - Formulate a null hypothesis (H0).
    - Formulate an alternative hypothesis (H1).
    - Ensure the hypotheses are relevant and testable where applicable.
    - If hypothesis testing is not appropriate, explain why.

    E. Data Requirements
    - Identify the data required to investigate the research questions.
    - Explain how the data could be collected.

    F. Limitations
    - Identify potential methodological limitations.

    Rules:
    - Align everything with the research questions and objectives.
    - Do not invent research findings.
    - Do not claim hypotheses have been tested without actual data.
    - Clearly distinguish recommendations from established facts.
    """,
    expected_output=(
        "A structured research methodology document containing "
        "the research approach, research design, variables, "
        "hypotheses, data requirements, and methodological limitations."
    ),
    agent=research_question_agent,
)