

from threading import RLock
from typing import Callable, Type


class Event:

    lock: RLock = RLock()
    def __init__(self, *args: Type) -> None:
        self.subscribers: list[Callable] = []
        self.args: tuple[Type, ...] = args

    def subscribe(self, func: Callable) -> None:
        if func not in self.subscribers:
            self.subscribers.append(func)

    def unsubscribe(self, func: Callable) -> None:
        if func in self.subscribers:
            self.subscribers.remove(func)

    def emit(self, *args) -> None:
        with self.lock:
            if len(args) == len(self.args):
                if any(not isinstance(arg, self_arg) for arg, self_arg in zip(args, self.args)):
                    raise TypeError(f'This event should emit next types: {self.args}, but you try to emit {args}.')
            else:
                raise TypeError(f'This event should emit next types: {self.args}, but you try to emit {args}.')
            [callback(*args) for callback in self.subscribers]
