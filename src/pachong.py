import time
import asyncio  # 协程


# async 修饰词声明异步函数，于是，这里的 crawl_page 和 main 都变成了异步函数。
# 而调用异步函数，我们便可得到一个协程对象（coroutine object）。

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    # time.sleep(sleep_time)
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    # for url in urls:
    #     await crawl_page(url)
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # for task in tasks:
    #     await task
    # *tasks
    # 解包列表，将列表变成了函数的参数；与之对应的是， ** dict
    # 将字典变成了函数的参数。
    await asyncio.gather(*tasks)


# main(['url_1', 'url_2', 'url_3', 'url_4'])
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
