import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    async with sse_client("http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            url = "https://www.geeksforgeeks.org/top-python-ide/"
            result = await session.call_tool("crawl_website", {"url": url})
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
