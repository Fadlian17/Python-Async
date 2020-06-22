# Get Movie Title

import requests
import aiohttp
import asyncio

api_keys = "5baf45214039cf9ae474a0d55c8939a4"


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        movies = await fetch(session, 'https://api.themoviedb.org/3/movie/top_rated?api_key=5baf45214039cf9ae474a0d55c8939a4')
        result = map(lambda m: "title : {} - vote : {}".format(
            m['title'], m['vote_average']), movies['results'])
        for m in result:
            print(m)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
