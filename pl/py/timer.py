class HashedWheelTimeout:
    def __init__(self):
        pass

class HashedWheelBucket:
    def __init__(self):
        pass

from enum import Enum
from typing import Deque

class TIMEOUT_ST(Enum):
    ST_INIT = 0
    ST_EXPIRED = 1
    ST_CANCELLED = 2

from collections import deque

class HashedWheelTimer:
    timeouts: Deque[HashedWheelTimeout] = deque()

    def start(self):
        pass

    def stop(self):
        pass

    def newTimeout(self):
        pass



from CountDownLatch import CountDownLatch


import unittest
class TimerTest(unittest.TestCase):
    # def setUp(self) -> None:
    #     return super().setUp()
    
    def testScheduleTimeoutShouldRunAfterDelay(self):
        print('================ Timer test')
        timer = HashedWheelTimer()
        barrier = CountDownLatch(1)
        # timeout = timer.newTimeout(barrier.count_down())
        pass

def main():
    print('main')


if __name__ == "__main__":
    # main()

    unittest.main()