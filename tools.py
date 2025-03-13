from smolagents import tool
import requests
from dotenv import load_dotenv
import os
from typing import Optional
from urllib.parse import urlencode
load_dotenv()

@tool
def get_topheadlines_by_query(
    query: str,
    from_date: str,
    to_date: str,
    sort_by: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        query: Keywords or a phrase to search for.
        from_date: A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        to_date: A date and optional time for the most recent article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        sort_by: The order to sort the articles in. Possible options: 
          - "relevancy" = articles more closely related to the query come first. 
          - "popularity" = articles from popular sources and publishers come first.
          - "publishedAt" = newest articles come first.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "API key is missing"}

    url = (
        f'https://newsapi.org/v2/everything?'
        f'q={query}'
        f'&from={from_date}&to={to_date}&sortBy={sort_by}'
        f'&apiKey={api_key}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}

@tool
def get_topheadlines_by_query_and_sources(
    query: str,
    sources: str,
    from_date: str,
    to_date: str,
    sort_by: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        query: Keywords or a phrase to search for.
        sources: A comma-separated string of news sources to fetch news from.
        from_date: A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        to_date: A date and optional time for the most recent article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        sort_by: The order to sort the articles in. Possible options: 
          - "relevancy" = articles more closely related to the query come first. 
          - "popularity" = articles from popular sources and publishers come first.
          - "publishedAt" = newest articles come first.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "API key is missing"}

    url = (
        f'https://newsapi.org/v2/everything?'
        f'q={query}&sources={sources}'
        f'&from={from_date}&to={to_date}&sortBy={sort_by}'
        f'&apiKey={api_key}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}

@tool
def get_topheadlines_by_sources(

    sources: str,
    from_date: str,
    to_date: str,
    sort_by: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        sources: A comma-separated string of news sources to fetch news from.
        from_date: A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        to_date: A date and optional time for the most recent article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        sort_by: The order to sort the articles in. Possible options: 
          - "relevancy" = articles more closely related to the query come first. 
          - "popularity" = articles from popular sources and publishers come first.
          - "publishedAt" = newest articles come first.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "API key is missing"}

    url = (
        f'https://newsapi.org/v2/everything?'
        f'sources={sources}'
        f'&from={from_date}&to={to_date}&sortBy={sort_by}'
        f'&apiKey={api_key}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}

@tool
def get_topheadlines_by_query_and_category(
    query: str,
    category: str,
    from_date: str,
    to_date: str,
    sort_by: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        query: Keywords or a phrase to search for.
        category: category: News category (e.g., business, sports).
        from_date: A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        to_date: A date and optional time for the most recent article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        sort_by: The order to sort the articles in. Possible options: 
          - "relevancy" = articles more closely related to the query come first. 
          - "popularity" = articles from popular sources and publishers come first.
          - "publishedAt" = newest articles come first.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "API key is missing"}

    url = (
        f'https://newsapi.org/v2/top-headlines?'
        f'q={query}&category={category}'
        f'&from={from_date}&to={to_date}&sortBy={sort_by}'
        f'&apiKey={api_key}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}

@tool
def get_topheadlines_by_category(
    category: str,
    from_date: str,
    to_date: str,
    sort_by: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        category: category: News category (e.g., business, sports).
        from_date: A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        to_date: A date and optional time for the most recent article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        sort_by: The order to sort the articles in. Possible options: 
          - "relevancy" = articles more closely related to the query come first. 
          - "popularity" = articles from popular sources and publishers come first.
          - "publishedAt" = newest articles come first.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "API key is missing"}

    url = (
        f'https://newsapi.org/v2/top-headlines?'
        f'category={category}'
        f'&from={from_date}&to={to_date}&sortBy={sort_by}'
        f'&apiKey={api_key}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}

@tool
def get_everything_by_query_and_sources(
    query: str,
    sources: str,
    from_date: str,
    to_date: str,
    sort_by: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        query: Keywords or a phrase to search for.
        sources: A comma-separated string of news sources to fetch news from.
        from_date: A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        to_date: A date and optional time for the most recent article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        sort_by: The order to sort the articles in. Possible options: 
          - "relevancy" = articles more closely related to the query come first. 
          - "popularity" = articles from popular sources and publishers come first.
          - "publishedAt" = newest articles come first.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "API key is missing"}

    url = (
        f'https://newsapi.org/v2/everything?'
        f'q={query}&sources={sources}'
        f'&from={from_date}&to={to_date}&sortBy={sort_by}'
        f'&apiKey={api_key}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}
@tool
def get_everything_by_query(
    query: str,
    from_date: str,
    to_date: str,
    sort_by: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        query: Keywords or a phrase to search for.
        from_date: A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        to_date: A date and optional time for the most recent article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        sort_by: The order to sort the articles in. Possible options: 
          - "relevancy" = articles more closely related to the query come first. 
          - "popularity" = articles from popular sources and publishers come first.
          - "publishedAt" = newest articles come first.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "API key is missing"}

    url = (
        f'https://newsapi.org/v2/everything?'
        f'q={query}'
        f'&from={from_date}&to={to_date}&sortBy={sort_by}'
        f'&apiKey={api_key}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}
@tool
def get_everything_by_sources(
    sources: str,
    from_date: str,
    to_date: str,
    sort_by: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        sources: A comma-separated string of news sources to fetch news from.
        from_date: A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        to_date: A date and optional time for the most recent article allowed. This should be in ISO 8601 format (e.g. 2025-03-12 or 2025-03-12T15:56:38).
        sort_by: The order to sort the articles in. Possible options: 
          - "relevancy" = articles more closely related to the query come first. 
          - "popularity" = articles from popular sources and publishers come first.
          - "publishedAt" = newest articles come first.

    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "API key is missing"}

    url = (
        f'https://newsapi.org/v2/everything?'
        f'sources={sources}'
        f'&from={from_date}&to={to_date}&sortBy={sort_by}'
        f'&apiKey={api_key}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}

@tool
def get_sources(
    category: str
) -> dict:
    """
    Fetches news articles based on filters.

    Args:
        category: category: News category (e.g., business, sports).
    Returns:
        dict: A dictionary containing the news articles and metadata.
    """

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "API key is missing"}

    url = (
        f'https://newsapi.org/v2/top-headlines/sources?'
        f'category={category}'
        f'&apiKey={api_key}'
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}



