from smolagents import CodeAgent, LiteLLMModel
from tools import get_topheadlines_by_query,get_topheadlines_by_query_and_sources,get_topheadlines_by_sources,get_topheadlines_by_category,get_everything_by_query,get_everything_by_query_and_sources,get_everything_by_sources,get_sources
from dotenv import load_dotenv
import os
load_dotenv()
model = LiteLLMModel(model_id="openai/gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")) # Could use 'gpt-4o'
agent = CodeAgent(tools=[get_topheadlines_by_query,get_topheadlines_by_query_and_sources,get_topheadlines_by_sources,get_topheadlines_by_category,get_everything_by_query,get_everything_by_query_and_sources,get_everything_by_sources,get_sources], model=model, add_base_tools=True)

result = agent.run("bring me 5 trump related news stories from march 2025. summarize them briefly and create a headline for each one. use the tools I gave you to do this.I want the output format as follows: Headline: <headline> Summary: <summary> Link: <link> Date: <date> Source: <source>")
print(result)