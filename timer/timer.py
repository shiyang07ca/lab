from abc import ABCMeta, abstractmethod


class Timer(metaclass=ABCMeta):

    def __init__(self):
        """Pass."""

    @abstractmethod
    def init_timer(self, ):
        """Pass."""

    @abstractmethod
    def add_entry(self, ):
        """Pass."""

    @abstractmethod
    def cancel_entry(self, ):
        """Pass."""

    @abstractmethod
    def expire_entry(self, ):
        """Pass."""

    @abstractmethod
    @property
    def entrys(self):
        """Pass."""


class TimeWheel(Timer):
    pass


def main():
    pass


def test_add_entry():
    pass


def test_get_all_entry():
    pass


if __name__ == '__main__':
    main()
