from dataclasses import dataclass
from typing import Optional


@dataclass
class MyClass:
    name: str
    age: Optional[int]
    email: Optional[str]


def t_dataclass():
    obj1 = MyClass("Alice", 25, "alice@example.com")
    obj2 = MyClass("Bob", None, None)

    print(obj1)  # 输出: MyClass(name='Alice', age=25, email='alice@example.com')
    print(obj2)  # 输出: MyClass(name='Bob', age=None, email=None)


if __name__ == "__main__":
    t_dataclass()
