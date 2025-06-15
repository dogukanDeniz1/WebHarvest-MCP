from mcp.server.fastmcp import FastMCP
from services.web_search import search_duckduckgo
from services.crawler import crawl_url
from utils.types import SearchResult, CrawlResult, SearchAndCrawlResult
from utils.logger import info, debug, fatal

mcp = FastMCP("WebSearch")

@mcp.tool()
def search_internet(query: str, max_results: int = 5) -> list[SearchResult]:
    """
    Search DuckDuckGo and return a list of result URLs.

    Args:
        query (str): The search query to use on DuckDuckGo.
        max_results (int, optional): Maximum number of results to return. Defaults to 5.

    Returns:
        list[SearchResult]: A list of search result objects, each with a 'url' field.
            - SearchResult: {"url": str}

    Example:
        >>> search_internet(query="python web frameworks", max_results=2)
        [
            SearchResult(url="https://realpython.com/tutorials/web-development/"),
            SearchResult(url="https://www.fullstackpython.com/web-frameworks.html")
        ]
    """
    debug(f"search_internet called with query='{query}', max_results={max_results}")
    links = search_duckduckgo(query=query, max_results=max_results)
    info(f"DuckDuckGo returned {len(links)} results for query '{query}'")
    return [SearchResult(url=link) for link in links]

@mcp.tool()
async def crawl_website(url: str) -> CrawlResult:
    """
    Crawl the given URL and return the crawled content as markdown.

    Args:
        url (str): The URL to crawl.

    Returns:
        CrawlResult: An object with the crawled URL and its content.
            - CrawlResult: {"url": str, "content": str}

    Example:
        >>> crawl_website(url="https://www.geeksforgeeks.org/top-python-ide/")
        CrawlResult(
            url="https://www.geeksforgeeks.org/top-python-ide/",
            content="# Top Python IDEs... (markdown content)"
        )
    """
    debug(f"crawl_website called with url='{url}'")
    content = await crawl_url(url)
    if content:
        info(f"Crawled content for url '{url}' (length={len(content)})")
    else:
        fatal(f"Crawling failed or returned no data for url '{url}'")
    return CrawlResult(url=url, content=content or "Crawling failed or returned no data.")

@mcp.tool()
async def search_and_crawl(query: str, max_results: int = 5) -> SearchAndCrawlResult:
    """
    Search DuckDuckGo for links and crawl each result, returning their content.

    Args:
        query (str): The search query to use on DuckDuckGo.
        max_results (int, optional): Maximum number of results to return. Defaults to 5.

    Returns:
        SearchAndCrawlResult: An object with a list of crawl results for each found URL.
            - SearchAndCrawlResult: {"results": List[CrawlResult]}
            - CrawlResult: {"url": str, "content": str}

    Example:
        >>> search_and_crawl(query="2025 champions league winner", max_results=2)
        SearchAndCrawlResult(results=[
            CrawlResult(url="https://en.wikipedia.org/wiki/2025_UEFA_Champions_League_final", content="# 2025 UEFA Champions League final..."),
            CrawlResult(url="https://www.uefa.com/uefachampionsleague/news/", content="# UEFA Champions League News...")
        ])
    """
    debug(f"search_and_crawl called with query='{query}', max_results={max_results}")
    links = search_duckduckgo(query=query, max_results=max_results)
    info(f"DuckDuckGo returned {len(links)} results for query '{query}' in search_and_crawl")
    results = []
    for url in links:
        debug(f"Crawling url: {url}")
        content = await crawl_url(url)
        if content:
            info(f"Crawled content for url '{url}' (length={len(content)}) in search_and_crawl")
        else:
            fatal(f"Crawling failed or returned no data for url '{url}' in search_and_crawl")
        results.append(CrawlResult(url=url, content=content or "Crawl failed or no data."))
    return SearchAndCrawlResult(results=results)



if __name__ == "__main__":
    mcp.run(transport="sse")