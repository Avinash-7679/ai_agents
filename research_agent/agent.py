from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import google_search
from google.adk.tools.agent_tool import AgentTool
from google.genai import types
from typing import List, Dict, Any

# Retry configuration
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# -------- Custom Tool --------
def count_papers(papers: List[str]) -> Dict[str, Any]:
    """Count the number of research papers."""
    if not isinstance(papers, list):
        return {"status": "error", "error_message": "Expected list of papers"}
    return {"status": "success", "count": len(papers)}

# -------- Sub-Agent --------
google_search_agent = LlmAgent(
    name="google_search_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    description="Searches for research papers using Google Search.",
    instruction="Use google_search to get a LIST of papers.",
    tools=[google_search],
)

# -------- Root Agent --------
root_agent = LlmAgent(
    name="research_paper_finder",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction=(
        "1. Use google_search_agent to search for research papers.\n"
        "2. Use count_papers() to count them.\n"
        "3. Return the final count and the list."
    ),
    tools=[
        AgentTool(agent=google_search_agent),
        count_papers,
    ],
)
