import signal
import sys
import asyncio
import aiohttp
import json


async def get_json(client, url):
    print("*****: " + url)
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def get_reddit_top(subreddit, client):
    print("------: " + subreddit)
    data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')
    print('DONE:', subreddit + '\n')

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)

tasks = [asyncio.ensure_future(get_reddit_top('python', client)),
        asyncio.ensure_future(get_reddit_top('programming', client)),
        asyncio.ensure_future(get_reddit_top('compsci', client))]

loop.run_until_complete(asyncio.wait(tasks))
loop.stop()
client.connector.close()