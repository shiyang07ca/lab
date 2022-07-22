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


import unittest


class TestSched(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_entry(self):
        pass

    def test_get_all_entry(self):
        pass


def main():
    import time
    from timer.scheduler import scheduler

    s = scheduler(time.time, time.sleep)

    def print_time(a='default'):
        print("From print_time", time.time(), a)

    def print_some_times():
        print(time.time())
        s.enter(10, 1, print_time)
        s.enter(5, 2, print_time, argument=('positional', ))
        s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
        s.run()
        print(time.time())

    import ipdb
    ipdb.set_trace()

    print_some_times()


if __name__ == '__main__':
    main()
