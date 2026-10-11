from crewai import Task
from multi_agent_1.agents.data_analysis_agent import data_analysis_agent

data_analysis_task=Task(
    description="""
      Develop a data collection and analysis plan for the research.

    Research Topic:
    {topic}

    Research Problem:
    {research_problem}

    Research Questions:
    {research_questions}

    Research Design:
    {research_design}

    Sampling Plan:
    {sampling_plan}

    Available Dataset Information:
    {dataset_information}

    Complete the following sections:

    A. Data Collection
    - Identify suitable primary or secondary data sources.
    - Recommend data collection methods.

    B. Data Preparation
    - Explain how missing values, duplicates, inconsistent
      records, and irrelevant data should be handled.

    C. Analysis Methods
    - Recommend appropriate statistical, machine-learning,
      or qualitative analysis methods.
    - Explain why each method fits the research questions.

    D. Hypothesis Testing
    - Recommend an appropriate test if hypothesis testing applies.
    - State the assumptions that must be checked.
    - Do not claim that a hypothesis has been tested without
      actual data and calculations.

    E. Evaluation
    - Identify appropriate evaluation metrics.
    - For machine-learning studies, consider precision, recall,
      F1-score, and confusion matrix where appropriate.

    F. Interpretation
    - Explain how results should be interpreted.
    - Identify limitations and potential sources of bias.

    Rules:
    - Do not fabricate datasets, sample sizes, metrics, or findings.
    - If no dataset is provided, give a proposed analysis plan.
    - Clearly distinguish proposed methods from completed analysis.
    """,

    expected_output=(
        "A structured data collection and analysis plan covering "
        "data sources, preparation, analytical methods, hypothesis "
        "testing, evaluation, interpretation, and limitations."
    ),
    
    agent=data_analysis_agent,
)