import asyncio

@asyncio.coroutine
def run_a(future):
    while True:
        print('A')
        yield from asyncio.sleep(1)

@asyncio.coroutine
def run_b(future):
    while True:
        print('B')
        yield from asyncio.sleep(3)

def got_result(future):
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop()
future = asyncio.Future()

asyncio.ensure_future(run_a(future))
asyncio.ensure_future(run_b(future))

try:
    loop.run_forever()
finally:
    loop.close()

