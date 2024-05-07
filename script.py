import aiohttp
import asyncio
import requests

from settings import (
    APPS,
    TEAMS_WEBHOOK_URL,
)


async def check_site_urls(session):
    return [{'response': session.get(site['url']), 
             'name': site['name']} for site in APPS]


async def check_apps_status():
    async with aiohttp.ClientSession() as session:
        tasks = await check_site_urls(session)

        responses = await asyncio.gather(
            *(task['response'] for task in tasks), 
            return_exceptions=True,
        )

        for task, response in zip(tasks, responses):
            if isinstance(response, Exception) or \
                response.status not in {200, 401}:

                async with session.post(
                    TEAMS_WEBHOOK_URL, 
                    json={'text': f'{task["name"]} is down'},
                ) as res:
                    
                    if res.status == 200:
                        print('Message sent')
                    else:
                        print('Failed to send message.')


loop = asyncio.get_event_loop()
loop.run_until_complete(check_apps_status())