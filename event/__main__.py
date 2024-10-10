import asyncio
from event import Event

async def foo(a1: float, a2: str):
    print(a1, a2)

def bar(a1: float, a2: str):
    print(a1, a2)

async def main():
    e = Event(int | float | str, str)
    e.subscribe(foo)
    e.emit(123, 'hello')
    await asyncio.sleep(0.2)

# asyncio.run(main())

def main2():
    e = Event(int | float | str, str)
    e.subscribe(foo)
    e.emit(123, 'hello')


if __name__ == '__main__':
    main2()