import asyncio

def callback(n):
    print(f'callback {n} invoked')

async def main(loop):
    print('register callbacks')
    now = loop.time()
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)
    loop.call_later(now + 1, callback, 4)
    # await asyncio.sleep(2)
    print('callbacks end')

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main(loop))
finally:
    loop.close()