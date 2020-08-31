import asyncio
import functools

"""等待Future完成并返回结果"""
# def callback(future, result):
#     print(f'setting future result to: {result}')
#     future.set_result(result)

# async def main(loop):
#     future = asyncio.Future()
#     loop.call_soon(callback, future, 'the result')
#     res = await future
#     print(f'return result: {res}')

# event_loop = asyncio.get_event_loop()
# try:
#     event_loop.run_until_complete(main(event_loop))
# finally:
#     event_loop.close()

"""Future设置回调"""
def callback(future, n):
    print(f'{n}: future done: {future.result()}')

async def register_callbacks(future: asyncio.Future):
    print('registering callbacks on future')
    future.add_done_callback(functools.partial(callback, n=1))
    future.add_done_callback(functools.partial(callback, n=2))

async def main(future):
    await register_callbacks(future)
    print('setting result of future')
    future.set_result('the result')

event_loop = asyncio.get_event_loop()
try:
    future = asyncio.Future()
    event_loop.run_until_complete(main(future))
finally:
    event_loop.close()