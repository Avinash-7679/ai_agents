from google.adk.agents import Agent
import os

# --- Step 1: Load Gemini API key ---
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ GOOGLE_API_KEY not found. Please set it first.")
    exit()

# --- Step 2: Create your Gemini Agent (new syntax) ---
agent = Agent(
    name="GeminiAgent",           # ✅ required field
    model="gemini-1.5-flash",     # model name
    config={"api_key": api_key},  # ✅ API key now goes inside config
)

# --- Step 3: Ask a question ---
query = "Who is the founder of SRM University AP?"
response = agent.run(query)

print("\n✅ Gemini Agent Response:")
print(response)
