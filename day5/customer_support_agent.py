# customer_support_agent.py

import asyncio
from google.adk.agents import LlmAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent, AGENT_CARD_WELL_KNOWN_PATH
from google.adk.models.google_llm import Gemini
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import uuid

# Retry options
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# Remote Agent (Product Catalog Agent running at port 8001)
remote_product_catalog_agent = RemoteA2aAgent(
    name="product_catalog_agent",
    description="Remote product catalog agent from external vendor.",
    agent_card=f"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}",
)

# Customer Support Agent
customer_support_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="customer_support_agent",
    description="A customer support assistant that looks up product information.",
    instruction="""
    Use product_catalog_agent to fetch all product info.
    Always check using the tool before responding.
    """,
    sub_agents=[remote_product_catalog_agent],
)

# Interactive chat loop
async def chat():
    print("\n=== Customer Support CLI Chatbot ===")
    print("Type 'exit' to quit.\n")

    session_service = InMemorySessionService()
    app_name = "support_app"
    user_id = "cli_user"
    session_id = f"cli_session_{uuid.uuid4().hex[:8]}"

    session = await session_service.create_session(
        app_name=app_name, user_id=user_id, session_id=session_id
    )

    runner = Runner(
        agent=customer_support_agent,
        app_name=app_name,
        session_service=session_service,
    )

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chatbot...")
            break

        test_content = types.Content(parts=[types.Part(text=user_input)])

        print("Assistant:", end=" ", flush=True)

        async for event in runner.run_async(
            user_id=user_id, session_id=session_id, new_message=test_content
        ):
            if event.is_final_response() and event.content:
                for part in event.content.parts:
                    if hasattr(part, "text"):
                        print(part.text)
        print()

if __name__ == "__main__":
    asyncio.run(chat())
