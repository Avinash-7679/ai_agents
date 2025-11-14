import asyncio
from google.adk.runners import InMemoryRunner
from research-agent.agent import root_agent

runner = InMemoryRunner(agent=root_agent)

async def main():
    print("🤖 Research Paper Finder Agent Running...")
    prompt = "Find recent research papers about quantum computing."
    response = await runner.run_debug(prompt)

    print("\n===== FINAL AGENT ANSWER =====\n")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
