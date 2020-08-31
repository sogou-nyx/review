import asyncio


async def outer():
    print('in outer')
    print('waiting for result1')
    await asyncio.ensure_future(phase1())
    print('waiting for result2')
    await asyncio.ensure_future(phase2())

async def phase1():
    print('in phase1')
    await asyncio.sleep(2)
    print('phase1 end')

async def phase2():
    print('in phase2')
    await asyncio.sleep(1)
    print('phase2 end')

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(outer())
finally:
    event_loop.close()