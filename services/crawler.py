from crawl4ai.docker_client import Crawl4aiDockerClient
from crawl4ai import BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.models import CrawlResult


from config import settings
from typing import Optional

async def crawl_url(url: str) -> CrawlResult:
    async with Crawl4aiDockerClient(base_url=settings.crawl4ai_docker_url, verbose=False) as client:
        try:
            bm25_filter = BM25ContentFilter(user_query=None, bm25_threshold=1.0)
            md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)

            crawler_config = CrawlerRunConfig(
                markdown_generator=md_generator,
                excluded_tags=["nav", "footer", "header", "form", "img", "a"],
                scan_full_page = True,  
                delay_before_return_html=0.5,
                only_text=True,
                remove_overlay_elements=True,
                exclude_social_media_domains=[
                                                "facebook.com",
                                                "twitter.com",
                                                "x.com",
                                                "linkedin.com",
                                                "instagram.com",
                                                "pinterest.com",
                                                "tiktok.com",
                                                "snapchat.com",
                                                "reddit.com"
                                            ],
                cache_mode=CacheMode.BYPASS,
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
            )
            browser_config = BrowserConfig(headless=True, text_mode=True, light_mode=True)

            await client.authenticate("user@example.com")
            results = await client.crawl(
                [url],
                browser_config=browser_config,
                crawler_config=crawler_config
            )

            if results.status_code == 200:
                return results.markdown
            return None
        except Exception as e:
            print(f"[crawl_url] Crawl error for {url}: {e}")
    return None
