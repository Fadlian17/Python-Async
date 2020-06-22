import requests
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        jsonplace = await fetch(session, 'https://jsonplaceholder.typicode.com/posts')
        for x in jsonplace:
            print("title:", x['title'])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
