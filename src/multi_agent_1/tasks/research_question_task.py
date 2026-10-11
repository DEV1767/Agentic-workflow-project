from crewai import Task
from multi_agent_1.agents.research_question_agent import research_question_agent

research_question_task=Task(
    description="""
      Develop research questions and objectives for the following study.

    Topic:
    {topic}

    Research Problem:
    {research_problem}

    Literature Review:
    {literature_review}

    Instructions:

    1. Identify the main research aim.
    2. Create one main research question.
    3. Create 3-5 specific research questions.
    4. Create one general research objective.
    5. Create 3-5 specific research objectives.
    6. Ensure every question is relevant to the research problem.
    7. Make objectives specific and measurable wherever possible.
    8. Do not invent findings or claim that a research gap is proven
       when the literature review provides insufficient evidence.

    Output format:

    A. Research Aim
    B. Main Research Question
    C. Specific Research Questions
    D. General Objective
    E. Specific Objectives
    F. Relationship Between Questions and Objectives
    """,

    expected_output=(
        "A structured set of research questions and measurable objectives "
        "aligned with the research problem and literature review."
    ),
    agent=research_question_agent

)
