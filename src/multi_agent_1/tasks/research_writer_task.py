from crewai import Task
from multi_agent_1.agents.researcher_writer_agent import research_writer_agent

research_writer_task=Task(
     description="""
    Write a structured research report using the supplied information.

    Research Topic:
    {topic}

    Research Problem:
    {research_problem}

    Literature Review:
    {literature_review}

    Research Questions and Objectives:
    {research_question}

    Research Design and Hypothesis:
    {research_design}

    Sampling Plan:
    {sampling_plan}

    Data Collection and Analysis:
    {data_analysis}

    Organize the report into these sections:

    1. Research Title
    2. Introduction
    3. Problem Statement
    4. Literature Review
    5. Research Questions
    6. Research Objectives
    7. Hypotheses, where applicable
    8. Research Methodology
    9. Sampling Strategy
    10. Data Collection and Analysis Plan
    11. Limitations
    12. Conclusion and Recommendations

    Rules:
    - Use only the supplied evidence for factual research claims.
    - Preserve source URLs and citations where available.
    - Do not invent references or research findings.
    - Clearly label proposed methods as proposals.
    - Do not present planned analysis as completed analysis.
    - Avoid unnecessary repetition.
    - Keep the report concise and academically structured.
    """,
   expected_output=(
     "A structured academic research report with clearly "
        "organized sections, evidence-based claims, and no "
        "fabricated references or results."
   ),
   agent=research_writer_agent,

)