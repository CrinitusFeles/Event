

from asyncio import iscoroutinefunction
import asyncio
from types import UnionType
from typing import Any, Callable, Coroutine, Type


class Event:
    def __init__(self, *args: Type | UnionType) -> None:
        self.subscribers: list[Callable[..., Coroutine | Any]] = []
        self.args: tuple[Type | UnionType, ...] = args

    def subscribe(self, func: Callable) -> None:
        if func not in self.subscribers:
            self.subscribers.append(func)

    def unsubscribe(self, func: Callable) -> None:
        if func in self.subscribers:
            self.subscribers.remove(func)

    def emit(self, *args) -> None:
        if len(args) == len(self.args):
            if any(not isinstance(arg, self_arg)
                    for arg, self_arg in zip(args, self.args)):
                raise TypeError(f'This event should emit next types: '\
                                f'{self.args}, but you try to emit {args}.')
        else:
            raise TypeError(f'This event should emit next types: '\
                            f'{self.args}, but you try to emit {args}.')
        for callback in self.subscribers:
            if iscoroutinefunction(callback):
                asyncio.create_task(callback(*args))
            else:
                callback(*args)
