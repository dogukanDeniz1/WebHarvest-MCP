from pydantic import BaseModel
from typing import List

class SearchResult(BaseModel):
    """
    Represents a single search result from DuckDuckGo.

    Attributes:
        url (str): The URL of the search result.
    """
    url: str

class CrawlResult(BaseModel):
    """
    Represents the result of crawling a single URL.

    Attributes:
        url (str): The URL that was crawled.
        content (str): The crawled content (usually in markdown or text format).
    """
    url: str
    content: str

class SearchAndCrawlResult(BaseModel):
    """
    Represents the combined result of searching and crawling multiple URLs.

    Attributes:
        results (List[CrawlResult]): A list of crawl results for each found URL.
    """
    results: List[CrawlResult]
