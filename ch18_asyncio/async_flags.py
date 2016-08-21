# Example 18-5 from FluentPython

import asyncio 
import aiohttp
from seqential import BASE_URL, save_flag, show, main

@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    img = yield from resp.read()
    return img

@asyncio.coroutine
def download_one(cc):
    img = yield from get_flag(cc)
    show(cc)
    save_flag(img, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    todo = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(todo)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)

if __name__ == '__main__':
    main(download_many)
