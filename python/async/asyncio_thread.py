import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

"""在python中使用asyncio执行异步的代码时，如果需要调用阻塞的io的方法，结合线程进行使用。在一个单独的线程中执行阻塞的代码"""
def block_task(i):
    print(f'task{i} start')
    time.sleep(0.5)
    print(f'task{i} done')

async def run_block_tasks(event_loop):
    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(excutor, block_task, i) for i in range(5)]
    await asyncio.wait(tasks)

excutor = ThreadPoolExecutor(max_workers=5)
event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(run_block_tasks(excutor))
finally:
    event_loop.close()
