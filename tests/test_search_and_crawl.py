import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    async with sse_client("http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool("search_and_crawl", {"query": "2025 champions league winner", "max_results": 3})
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
