import os
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool
from google.adk.code_executors import BuiltInCodeExecutor

# ---------- Function Tools ----------
def get_fee_for_payment_method(method: str) -> dict:
    """Return transaction fee percentage for a given payment method."""
    fee_database = {
        "platinum credit card": 0.02,   # 2%
        "gold debit card": 0.035,       # 3.5%
        "bank transfer": 0.01           # 1%
    }
    fee = fee_database.get(method.lower())
    if fee is not None:
        return {"status": "success", "fee_percentage": fee * 100}
    return {"status": "error", "error_message": f"Payment method '{method}' not found"}

def get_exchange_rate(base_currency: str, target_currency: str) -> dict:
    """Return mock exchange rate between two currencies."""
    rate_database = {"usd": {"eur": 0.93, "inr": 83.58}}
    base = base_currency.lower()
    target = target_currency.lower()
    rate = rate_database.get(base, {}).get(target)
    if rate is not None:
        return {"status": "success", "rate": rate}
    return {"status": "error", "error_message": f"Unsupported currency pair: {base}/{target}"}

# ---------- Calculation Agent ----------
calculation_agent = LlmAgent(
    name="CalculationAgent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction=(
        "You are a calculator that only responds with Python code "
        "that prints the result."
    ),
    code_executor=BuiltInCodeExecutor(),
)

# ---------- Enhanced Currency Agent ----------
enhanced_currency_agent = LlmAgent(
    name="enhanced_currency_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction=(
        "Use get_fee_for_payment_method and get_exchange_rate tools. "
        "Delegate math to calculation_agent."
    ),
    tools=[get_fee_for_payment_method, get_exchange_rate, AgentTool(agent=calculation_agent)],
)

runner = InMemoryRunner(agent=enhanced_currency_agent)

async def main():
    response = await runner.run_debug(
        "Convert 1250 USD to INR using Bank Transfer. Show precise calculation."
    )
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
