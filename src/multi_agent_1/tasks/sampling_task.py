from crewai import Task
from multi_agent_1.agents.sampling_agent import sampling_agent

sampling_task=Task(
     description="""
    Develop a sampling plan for the research study.

    Research Topic:
    {topic}

    Research Problem:
    {research_problem}

    Research Questions:
    {research_question}

    Research Design:
    {research_design}

    Prepare the following sections:

    A. Target Population
    - Identify the population relevant to the study.

    B. Sampling Frame
    - Explain how potential participants or data sources could
      be identified.

    C. Sampling Technique
    - Recommend a suitable probability or non-probability
      sampling technique.
    - Explain why it is appropriate.

    D. Sample Size
    - Recommend how sample size should be determined.
    - State assumptions and limitations.
    - Do not invent statistical calculations or claim that a
      sample size is statistically sufficient without evidence.

    E. Inclusion and Exclusion Criteria
    - Explain what should be included and excluded.

    F. Sampling Bias and Limitations
    - Identify potential biases and ways to reduce them.

    Rules:
    - Align the sampling plan with the research objectives.
    - Do not invent population statistics.
    - If information is missing, clearly state the assumptions.
    - If the study uses existing datasets instead of human
      participants, adapt the sampling plan accordingly.
    """,

    expected_output=(
        "A structured sampling plan describing the target "
        "population, sampling frame, technique, sample size "
        "considerations, eligibility criteria, and limitations."
    ),

    agent=sampling_agent,
)