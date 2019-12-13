import asyncio
import random


# 生产者和消费者，协程
# 消费者
async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{} get a val: {}'.format(id, val))
        await asyncio.sleep(1)


# 生产者
async def producer(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await queue.put(val)
        print('{} put a val: {}'.format(id, val))
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()

    customer_1 = asyncio.create_task(consumer(queue, 'customer_1'))
    customer_2 = asyncio.create_task(consumer(queue, 'customer_2'))

    producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
    producer_2 = asyncio.create_task(producer(queue, 'producer_2'))

    # 超过十秒，消费者取消任务
    await asyncio.sleep(10)
    customer_1.cancel()
    customer_2.cancel()

    await asyncio.gather(customer_1, customer_2, producer_1, producer_2, return_exceptions=True)


asyncio.run(main())
