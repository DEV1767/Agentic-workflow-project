from crewai import Task

from multi_agent_1.agents.literature_agent import literature_agent


literature_task = Task(
    description="""
    Conduct a literature review on the following research topic:

    Topic: {topic}

    Research Problem:
    {research_problem}

    Retrieved Research Evidence:
    {search_results}

    Follow these instructions strictly:

    1. EVIDENCE-BASED WRITING
       Use only the supplied research evidence to describe individual studies.
       Do not invent research papers, authors, methods, findings, or statistics.

    2. SOURCE INFORMATION
       For each study, include:
       - Paper title
       - Publication year
       - Research method, if stated in the evidence
       - Findings, if stated in the evidence
       - Source URL

    3. HANDLE MISSING INFORMATION
       If the method or findings are not available, explicitly write:
       "Not established from the retrieved evidence."

    4. RESEARCH LIMITATIONS
       Distinguish limitations explicitly stated by a paper from limitations
       inferred from the supplied abstract.
       Label your own inferences clearly.

    5. RESEARCH GAPS
       Identify possible research gaps based on the supplied evidence.
       Do not claim that a gap exists across the entire research field
       based on only a few papers.

    6. CITATIONS
       Use only the supplied titles, years, and URLs.
       Never generate a DOI, URL, author name, accuracy score, or citation
       that is absent from the evidence.

    7. OUTPUT FORMAT

       A. Introduction
       B. Review of Retrieved Studies
       C. Comparison of Research Methods and Findings
       D. Limitations of Available Evidence
       E. Potential Research Gaps
       F. Conclusion

    8. EVIDENCE LIMITATION
       State how many studies were reviewed.
       Clearly mention when the available evidence is insufficient
       to support a strong conclusion.
    """,

    expected_output="""
    A structured literature review containing:
    1. An introduction to the research topic.
    2. A review of each retrieved study with its title, year, and URL.
    3. A comparison of supported methods and findings.
    4. Explicitly distinguished limitations and inferences.
    5. Evidence-based potential research gaps.
    6. A conclusion that acknowledges the limitations of the available evidence.
    """,

    agent=literature_agent,
)