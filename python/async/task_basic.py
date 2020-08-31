import asyncio
import time

"""
Tasks是与事件循环交互的主要方式之一。Tasks会包装协程并对其运行状态进行追踪。
Tasks是Future的子类，所以其他协程也能够等待它们，并且每一个Task在任务完成后都有一个可被检索到的结果。
"""

# create task
# async def task_func():
#     print('in task_func')
#     return 'the result'

# async def main(loop):
#     print('creating task')
#     task = loop.create_task(task_func())
#     print('waiting for {!r}'.format(task))
#     return_value = await task
#     print('task completed {!r}'.format(task))
#     print('return value: {!r}'.format(return_value))

# event_loop = asyncio.get_event_loop()
# try:
#     event_loop.run_until_complete(main(event_loop))
# finally:
#     event_loop.close()

# 从协程创建Task
# async def wrapped():
#     print('wrapped')
#     return 'result'    

# async def inner(task):
#     print('inner: starting')
#     print('inner: waiting for {!r}'.format(task))
#     result = await task
#     print('inner: task returned {!r}'.format(result))

# async def main():
#     print('starter: creating task')
#     task = asyncio.ensure_future(wrapped())
#     print('starter: waiting for inner')
#     await inner(task)
#     print('starter: inner returned')

# event_loop = asyncio.get_event_loop()
# try:
#     event_loop.run_until_complete(main())
# finally:
#     event_loop.close()

# 并发测试1，task必须await
# async def msg(text):
#     await asyncio.sleep(0.1)
#     print(text)


# async def long_operation():
#     print('long_operation started')
#     await asyncio.sleep(3)
#     print('long_operation finished')


# async def main():
#     await msg('first')

#     # Now you want to start long_operation, but you don't want to wait it finised:
#     # long_operation should be started, but second msg should be printed immediately.
#     # Create task to do so:
#     task = asyncio.ensure_future(long_operation())
    
#     await msg('second')

#     # Now, when you want, you can await task finised:
#     await task


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())


# 并发测试2
async def testa(x):
    print("in test a")
    await asyncio.sleep(3)
    print("Resuming a")
    return x


async def testb(x):
    print("in test b")
    await asyncio.sleep(1)
    print('Resuming b')
    return x


async def main():
    start = time.time()
    # 串行执行
    # resulta = await testa(1)
    # resultb = await testb(2)
    #并行执行，gather、wait和创建task三种方法
    # resulta, resultb =  await asyncio.gather(testa(1), testb(2))
    # done, pending = await asyncio.wait([testa(1), testb(2)])
    task1 = asyncio.ensure_future(testa(1))
    task2 = asyncio.ensure_future(testb(2))
    await task1
    await task2
    # for next_to_complete in asyncio.as_completed([testa(1), testb(2)]):
        # await next_to_complete
    print("use %s time"%(time.time()-start))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())