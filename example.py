from pyprofyler import PyProfyler
import asyncio

@PyProfyler
def normal_func(n):
    return sum(range(n))

@PyProfyler
def normal_gen(n):
    for i in range(n):
        yield i*i

@PyProfyler
async def async_func(n):
    await asyncio.sleep(0.0000001)
    return n*n

@PyProfyler
async def async_gen(n):
    for i in range(n):
        await asyncio.sleep(0.0000001)
        yield i*i

print(normal_func(100000))
print(str(normal_func))

for v in normal_gen(5):
    print(v)
print(str(normal_gen))

async def main():
    print(await async_func(10))
    print(str(async_func))

    async for v in async_gen(5):
        print(v)
    print(str(async_gen))

asyncio.run(main())
