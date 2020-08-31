import asyncio
import functools

"""Lock"""
# def unlock(lock):
#     print('callback releasing lock')
#     lock.release()

# async def coro1(lock):
#     print('coro1 waiting for the lock')
#     async with lock:
#         print('coro1 acquired lock')
#     print('coro1 released lock')

# async def coro2(lock):
#     print('coro2 waiting for the lock')
#     await lock.acquire()
#     try:
#         print('coro2 acquired lock')
#     finally:
#         print('coro2 released lock')
#         lock.release()

# async def main(loop):
#     lock = asyncio.Lock()
#     print('acquiring the lock before starting coroutines')
#     await lock.acquire()
#     print('lock acquired: {}'.format(lock.locked()))
#     loop.call_later(1, functools.partial(unlock, lock))
#     print('waiting for coroutines')
#     await asyncio.wait([coro1(lock), coro2(lock)])

# event_loop = asyncio.get_event_loop()
# try:
#     event_loop.run_until_complete(main(event_loop))
# finally:
#     event_loop.close()

"""Event，相比较Lock，所有任务在event状态设置后可以同时开始，而使用lock时同一时刻只有一个任务可以获取lock然后执行"""
# def set_event(event):
#     print('setting event in callback')
#     event.set()

# async def coro1(event):
#     print('coro1 waiting for event')
#     await event.wait()
#     print('coro1 triggered')

# async def coro2(event):
#     print('coro2 waiting for event')
#     await event.wait()
#     print('coro2 triggered')

# async def main(loop):
#     event = asyncio.Event()
#     print('event start state: {}'.format(event.is_set()))
#     loop.call_later(0.5, functools.partial(set_event, event))
#     await asyncio.wait([coro1(event), coro2(event)])
#     print('event end state: {}'.format(event.is_set()))

# event_loop = asyncio.get_event_loop()
# try:
#     event_loop.run_until_complete(main(event_loop))
# finally:
#     event_loop.close()

"""Condition，类似java的锁，需要notify唤醒任务"""
# async def consumer(condition, n):
#     async with condition:
#         print('consumer {} is waiting'.format(n))
#         await condition.wait()
#         print('consumer {} triggered'.format(n))
#     print('ending consumer {}'.format(n))

# async def control_consumer(condition):
#     print('starting manipulate_condition')
#     await asyncio.sleep(0.5)
#     for i in range(1, 3):
#         async with condition:
#             print('notifying {} consumers'.format(i))
#             condition.notify(i)
#         await asyncio.sleep(0.5)
#     async with condition:
#         print('notifying remaining consumers')
#         condition.notify_all()
#     print('ending manipulate_condition')

# async def main(loop):
#     condition = asyncio.Condition()
#     consumers = [consumer(condition, i) for i in range(5)]
#     task = asyncio.ensure_future(control_consumer(condition))
#     await asyncio.wait(consumers)

# event_loop = asyncio.get_event_loop()
# try:
#     event_loop.run_until_complete(main(event_loop))
# finally:
#     event_loop.close()

#Queue
