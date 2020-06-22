# Json Cloudinary
import requests
import aiohttp
import asyncio
import json


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        food_product = await fetch(session, 'https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json')
        food_filter = filter(
            lambda tp: tp['category'] == 'fruits', food_product)
        print(json.dumps(list(food_filter), indent=2))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
