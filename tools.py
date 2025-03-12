from smolagents import tool
import requests
from dotenv import load_dotenv
import os
from typing import Optional
from urllib.parse import urlencode
load_dotenv()
@tool
def get_topheadlines() -> dict:
    """
    Fetches top news articles as a dictionary.

    Returns:
        dict: A dictionary containing the top news articles and metadata.
    """
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='+os.getenv('NEWS_API_KEY')
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        return {"error": f"Request failed with status code {response.status_code}"}


@tool
def get_topheadlines_by_query(
    query: str
) -> dict:
    """
    Fetches news articles based on the provided query and sorting order.

    Args:
        query : Keywords or a phrase to search for.
    Returns:
        dict: A dictionary containing the news articles and metadata.
    """
    url = (
        f'https://newsapi.org/v2/everything?'
        f'q={query}'
        f'&apiKey={os.getenv("NEWS_API_KEY")}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
@tool
def get_topheadlines_by_category(
    category: str
) -> dict:
    """
    Fetches news articles based on the provided query and sorting order.

    Args:
        category : The category you want to get headlines for. Possible options: business, entertainment, general health,science, sports,technology. 

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """
    url = (
        f'https://newsapi.org/v2/everything?'
        f'category={category}'
        f'&apiKey={os.getenv("NEWS_API_KEY")}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
@tool
def get_topheadlines_by_sources(
    sources: str
) -> dict:
    """
    Fetches news articles based on the provided query and sorting order.

    Args:
        sources: A comma-seperated string of identifiers for the news sources or blogs you want headlines from.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """
    url = (
        f'https://newsapi.org/v2/everything?'
        f'sources={sources}'
        f'&apiKey={os.getenv("NEWS_API_KEY")}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
@tool
def get_everything_by_query(
    query: str
) -> dict:
    """
    Fetches news articles based on the provided query and sorting order.

    Args:
        query : Keyword to search for in the news articles.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """
    url = (
        f'https://newsapi.org/v2/everything?'
        f'q={query}'
        f'&apiKey={os.getenv("NEWS_API_KEY")}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
@tool
def get_everything_by_category(
    category: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        sources (str): A comma-separated string of news sources to fetch news from.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    url = (
        f'https://newsapi.org/v2/everything?'
        f'category={category}'
        f'&apiKey={os.getenv("NEWS_API_KEY")}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

@tool
def get_everything_by_sources(
    sources: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        sources (str): A comma-separated string of news sources to fetch news from.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    url = (
        f'https://newsapi.org/v2/everything?'
        f'sources={sources}'
        f'&apiKey={os.getenv("NEWS_API_KEY")}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
result = get_everything_by_sources("bbc-news")
print(result)