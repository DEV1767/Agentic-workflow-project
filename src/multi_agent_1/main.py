import sys
from multi_agent_1.graph import research_graph

# Ensure Windows PowerShell/cmd console handles UTF-8 characters
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def run_research(topic: str) -> dict:
    """Run the complete research workflow."""

    initial_state = {
        "topic": topic,
        "research_problem": "",
        "literature_review": "",
        "research_question": "",
        "research_design": "",
        "sampling_plan": "",
        "data_analysis": "",
        "final_report": "",
    }

    result = research_graph.invoke(initial_state)
    return result


if __name__ == "__main__":
    topic = input("Enter your research topic: ").strip()

    if not topic:
        print("Please enter a research topic.")
    else:
        result = run_research(topic)
        final_report = result["final_report"]

        print("\n========== FINAL RESEARCH REPORT ==========\n")
        print(final_report)

        with open("research_report.md", "w", encoding="utf-8") as f:
            f.write(final_report)
        print("\nReport successfully saved to research_report.md!")

