from dataclasses import dataclass
from typing import Optional
from typing import Union


@dataclass
class MyClass:
    name: str
    age: Optional[int]
    email: Optional[str]


class Test:
    a: str
    b: int

    def log(self):
        pass


def t_dataclass():
    obj1 = MyClass("Alice", 25, "alice@example.com")
    obj2 = MyClass("Bob", None, None)

    print(obj1)  # 输出: MyClass(name='Alice', age=25, email='alice@example.com')
    print(obj2)  # 输出: MyClass(name='Bob', age=None, email=None)


def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token


from collections.abc import Iterable
from typing import Protocol, Any, TypeVar


class SupportsLessThan(Protocol):

    def __lt__(self, other: Any) -> bool:
        return self < other


LT = TypeVar('LT', bound=SupportsLessThan)


def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


if __name__ == "__main__":
    # t_dataclass()

    # parse_token(1)

    ss = range(8)
    print(top(ss, 4))

    # import ipdb; ipdb.set_trace()

    pass
