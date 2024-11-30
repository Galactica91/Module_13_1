import asyncio
import time

async def start_strongman(name, power, start_time):
    print(f'[{time.time() - start_time:.2f} сек] Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'[{time.time() - start_time:.2f} сек] Силач {name} поднял {i} шар')
    print(f'[{time.time() - start_time:.2f} сек] Силач {name} закончил соревнования')


async def start_tournament():
    start_time = time.time()

    strongman1 = asyncio.create_task(start_strongman('Pasha', 3, start_time))
    strongman2 = asyncio.create_task(start_strongman('Denis', 4, start_time))
    strongman3 = asyncio.create_task(start_strongman('Apollon', 5, start_time))

    await strongman1
    await strongman2
    await strongman3

    print(f'Общее время соревнований: {time.time() - start_time:.2f} сек')

if __name__ == '__main__':
    asyncio.run(start_tournament())