# Json List

import requests
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        product = await fetch(session, 'https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json')
        total_product = list(map(lambda tp: tp['price'], product))
        print("Total Harga Produk:", sum(total_product))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
