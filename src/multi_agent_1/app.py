from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from multi_agent_1.graph import research_graph

app=FastAPI(title="AI Research Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  
        "http://localhost:3000",  
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    topic:str

@app.get("/")
def home():
    return {"message":"AI Research Assistant API is running"}

@app.post("/research")
def conduct_research(request: ResearchRequest):
    topic = request.topic.strip()

    if not topic:
        raise HTTPException(
            status_code=400,
            detail="Research topic cannot be empty",
        )

    # Initial state for LangGraph
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

    try:
        result = research_graph.invoke(initial_state)

        return {
            "topic": topic,
            "report": result.get("final_report", ""),
        }

    except Exception as e:
        # Print the actual error in your terminal for debugging
        print(f"Research generation failed: {e}")

        raise HTTPException(
            status_code=500,
            detail="Research generation failed. Check the backend terminal.",
        )