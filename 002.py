# json Users
import requests
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        jsonuser = await fetch(session, 'https://jsonplaceholder.typicode.com/users')
        for u in jsonuser:
            print("alamat:", u['address']['street'], u['address']
                  ['suite'], u['address']['city'], u['address']['zipcode'])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
