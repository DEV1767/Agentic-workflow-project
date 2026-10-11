from crewai import Task
from multi_agent_1.agents.problem_agent import problem_agent

problem_task=Task(
    description="""
    Identify and define the research problem.

    Research Topic:
    {topic}

    Prepare the following sections:

    1. Background of the problem.
    2. Clear problem statement.
    3. Why the problem matters.
    4. Who is affected by the problem.
    5. Scope of the research.
    6. Potential research gap.

    Rules:
    - Do not invent statistics or research findings.
    - Do not claim a research gap is established without evidence.
    - Clearly distinguish assumptions from verified facts.
    - Keep the response concise and structured.
    """,

    expected_output=(
        "A structured research problem definition containing "
        "the background, problem statement, significance, "
        "affected population, scope, and potential research gap."
    ),

    agent=problem_agent,
)