# Event
Simple event implementation

## Installation

```
poetry add git+https://github.com/CrinitusFeles/Event.git
```

or

```
pip install git+https://github.com/CrinitusFeles/Event.git
```

## Using

``` python
def handler(arg: int)
    print(arg)

my_event = Event(int)
my_event.subscribe(handler)
...
# something happend
...
my_event.emit(123)

```