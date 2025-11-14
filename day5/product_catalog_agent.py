from google.adk.agents import LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.google_llm import Gemini
from google.genai import types

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

# PRODUCT LOOKUP TOOL
def get_product_info(product_name: str) -> str:
    catalog = {
        "iphone 15 pro": "iPhone 15 Pro, $999, Low Stock (8 units), 128GB, Titanium finish",
        "sony wh-1000xm5": "Sony WH-1000XM5, $399, In Stock (67 units), Noise-canceling, 30hr battery",
        "dell xps 15": "Dell XPS 15, $1,299, In Stock (45 units), 16GB RAM, 512GB SSD",
    }
    name = product_name.lower().strip()
    if name in catalog:
        return catalog[name]
    return f"Sorry, no details for {product_name}."

product_catalog_agent = LlmAgent(
    name="product_catalog_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    description="Provides product information.",
    instruction="Use get_product_info to return product details.",
    tools=[get_product_info],
)

# EXPOSE AS A2A APP ON PORT 8001
app = to_a2a(product_catalog_agent, port=8001)
