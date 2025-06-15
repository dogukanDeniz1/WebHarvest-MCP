# WebHarvest-MCP

## Project Purpose

This project is a **Model Context Protocol (MCP) server** implemented in Python. Its purpose is to perform web searches via DuckDuckGo and automatically crawl (scrape) the resulting pages to extract their content. The project is designed for easy integration with LLM-based applications or any other MCP-compatible clients.

## Disclaimer
**This project is provided as-is, without any warranty or guarantee of fitness for any purpose. The author assumes no responsibility for any use, misuse, or consequences arising from this software. Use at your own risk.**

## Features
- Search DuckDuckGo by keyword
- Automatically crawl (scrape) links from search results
- Expose all functionality via the MCP protocol
- Modern, extensible Python codebase
- Dependency management with the UV package manager
- Clean, structured output types (using Pydantic models)

## Use Cases
- Up-to-date web search and content gathering in LLM-based assistants
- Automated information collection and summarization applications
- Integration with any MCP-compatible client

## Requirements
- This project **requires a running [crawl4ai](https://github.com/unclecode/crawl4ai) service** for crawling and extracting web page content. You must have crawl4ai running and set the `CRAWL4AI_DOCKER_URL` in your `.env` file accordingly.

## Installation

### 1. Install Dependencies
This project uses [uv](https://github.com/astral-sh/uv) as the package manager. To install dependencies:

```powershell
uv pip install -r pyproject.toml
```
or
```powershell
uv venv
uv pip install -r pyproject.toml
```

Alternatively, for classic pip installation (not recommended):
```powershell
pip install -r requirements.txt  # If you have generated a requirements.txt
```

### 2. Environment Variables
Configure crawler service and log level in your `.env` file:

```
CRAWL4AI_DOCKER_URL=http://localhost:11235/md
LOG_LEVEL=INFO
```

## Running the Server

```powershell
uv run websearch.py
```
or
```powershell
python websearch.py
```

The server runs with SSE (Server-Sent Events) transport by default and can be integrated directly with MCP Inspector, Claude Desktop, Cursor, and similar clients.

## Provided MCP Tools

### 1. `search_internet`
Performs a DuckDuckGo search and returns the result links.

**Parameters:**
- `query` (str): The search keyword
- `max_results` (int): Maximum number of results (default: 5)

**Return Type:**
- `[SearchResult]` → `{ "url": str }`

### 2. `crawl_website`
Crawls a given URL and returns its content as markdown.

**Parameters:**
- `url` (str): The web address to crawl

**Return Type:**
- `CrawlResult` → `{ "url": str, "content": str }`

### 3. `search_and_crawl`
Performs a search, crawls each resulting link, and returns their content.

**Parameters:**
- `query` (str): The search keyword
- `max_results` (int): Maximum number of results (default: 5)

**Return Type:**
- `SearchAndCrawlResult` → `{ "results": [ { "url": str, "content": str }, ... ] }`

## Tests
All tests are located in the `tests/` directory as separate files. To test each tool and function, run the relevant file:

```powershell
python tests/test_search_internet.py
python tests/test_crawl_website.py
python tests/test_search_and_crawl.py
python tests/test_list_tools.py
```

## Developer Notes
- Be sure to include both `pyproject.toml` and `uv.lock` in your repository for dependency and environment management.
- Exclude `.env`, `.venv/`, `__pycache__/`, etc. using `.gitignore`.
- All types and example outputs are clearly explained in the code using Pydantic models and function docstrings.

## Potential Improvements
- Add support for other search engines (Google, Bing, etc.)
- Add advanced filtering or summarization of crawled content
- Add authentication and rate limiting for public deployments
- Add Dockerfile for easy containerization
- Add a web UI for manual search and crawl
- Add more detailed error handling and logging
- Add support for streaming large crawl results

## Contributing & License
Pull requests and issues are welcome. This project is licensed under the MIT License.

---

**Author:** Mehmet Doğukan Deniz

**Disclaimer:**
This project is provided for educational and research purposes only. The author disclaims all liability for any damages or consequences resulting from the use of this software. You are solely responsible for your use of this project.

