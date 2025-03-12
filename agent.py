from smolagents import CodeAgent, LiteLLMModel
from tools import get_news
from dotenv import load_dotenv
import os
load_dotenv()
model = LiteLLMModel(model_id="openai/gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")) # Could use 'gpt-4o'
agent = CodeAgent(tools=[get_news], model=model, add_base_tools=True)

result = agent.run("Take the news with the tools provided to you, extract article information from that news, and then summarize that information yourself.")
print(result)