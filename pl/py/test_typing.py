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

    def __init__(self):
        pass

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


LT = TypeVar("LT", bound=SupportsLessThan)


def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


class MyClass:
    class_var = 10

    def __init__(self, instance_var):
        self.instance_var = instance_var

    def print_vars(self):
        print("Class variable:", MyClass.class_var)
        print("Instance variable:", self.instance_var)

    @classmethod
    def set_class_var(cls):
        cls.class_var = 100


def t_class_var():
    a = MyClass(5)
    b = MyClass(6)
    a.print_vars()
    b.print_vars()

    a.instance_var = 8
    b.instance_var = 9
    a.print_vars()
    b.print_vars()

    # a.class_var = 20
    # b.class_var = 40
    # a.print_vars()
    # b.print_vars()

    a.set_class_var()
    a.print_vars()
    b.print_vars()

    MyClass.class_var = 30
    a.print_vars()
    b.print_vars()


if __name__ == "__main__":
    t_class_var()

    # t_dataclass()

    # parse_token(1)

    # ss = range(8)
    # print(top(ss, 4))

    # import ipdb; ipdb.set_trace()

    pass
