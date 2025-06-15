from duckduckgo_search import DDGS

def search_duckduckgo(query: str, max_results: int = 5) -> list[str]:
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        return [r["href"] for r in results if "href" in r]
