from smolagents import CodeAgent, LiteLLMModel
from tools import get_topheadlines_by_query, get_topheadlines_by_query_and_sources, get_topheadlines_by_sources, get_topheadlines_by_category, get_everything_by_query, get_everything_by_query_and_sources, get_everything_by_sources, get_sources
from dotenv import load_dotenv
import os

load_dotenv()
model = LiteLLMModel(model_id="openai/gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")) # Could use 'gpt-4o'
agent = CodeAgent(tools=[get_topheadlines_by_query, get_topheadlines_by_query_and_sources, get_topheadlines_by_sources, get_topheadlines_by_category, get_everything_by_query, get_everything_by_query_and_sources, get_everything_by_sources, get_sources], model=model, add_base_tools=True)

from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  
@app.route('/get-news', methods=['POST'])
def get_news():
    try:
        data = request.get_json()
        
        newstype = data.get('newstype')  
        query = data.get('query')  
        sources = data.get('source')  
        category = data.get('category') 
        fromdate = data.get('fromdate') 
        todate = data.get('toDate')  
        sortby = data.get('sortby')  

       
        news_query = f"""
            bring me news about {query} type of  {newstype} news. the date should be from {fromdate} to {todate}, sorted by {sortby}.
            Sources: {', '.join(sources)}. If some parameters are empty, just ignore them.
            Summarize them briefly and create a headline for each one.News summaries should be 75 words
            maximum number of news you can select 12.
            Use the tools I gave you to do this. I want the output format as follows:
            {{Headline: <headline> Summary: <summary> Link: <link> Date: <date> Source: <source> urlToImg: <urlToImg>}}
            If you give me any output other than this, I will find you and kill you.
            """

        result = agent.run(news_query)
        print(result)
        return jsonify({
            'success': True,
            'data': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
