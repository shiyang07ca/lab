from datetime import datetime
from enum import Enum
import json
from typing import Deque
from collections import deque

from redis import StrictRedis

from CountDownLatch import CountDownLatch


class TIMEOUT_ST(Enum):
    ST_INIT = 0
    ST_EXPIRED = 1
    ST_CANCELLED = 2


class HashedWheelTimeout:
    def __init__(self):
        pass


class HashedWheelBucket:
    def __init__(self):
        pass


class HashedWheelTimer:
    timeouts: Deque[HashedWheelTimeout] = deque()

    def start(self):
        pass

    def stop(self):
        pass

    def tick(self):
        pass

    def newTimeout(self):
        pass


def get_redis():
    conn = StrictRedis.from_url("redis://127.0.0.1/0", decode_responses=True)
    return conn


class RedTimerEntry:
    def __init__(
        self,
        name=None,
        task=None,
        schedule=None,
        args=None,
        kwargs=None,
        enabled=True,
        options=None,
        **clsargs,
    ):
        pass

    @classmethod
    def from_key(cls, key):
        with get_redis().pipeline() as pipe:
            pipe.hget(key, "definition")
            pipe.hget(key, "meta")
            definition, meta = pipe.execute()

        if not definition:
            raise KeyError(key)

        definition = json.loads(definition)
        meta = json.loads(meta)
        definition.update(meta)

        entry = cls(**definition)
        entry.last_run_at = meta["last_run_at"]

        return entry

    ...


# TODO: redis 分布式锁
class RedTimer:
    max_interval = 30

    schedule_key = "TIMER"

    schedule_dict = {}

    def start(self):
        for name, entry in RedTimer.schedule_dict.items():
            pass

    def stop(self):
        """释放锁, 退出进程"""
        pass

    @property
    def schedule(self):
        print("Timer: Get tasks")

        client = get_redis()
        max_due_at = int(datetime.now().timestamp())
        with client.pipeline() as pipe:
            pipe.zrangebyscore(RedTimer.max_interval, 0, max_due_at)

            due_tasks = pipe.execute()

        s = {}
        for key in due_tasks:
            print(f"key: {key}")

    def tick(self):
        pass

    def newTimeout(self):
        pass

    ...


import unittest

# def testScheduleTimeoutShouldRunAfterDelay(self):
#     print('================ Timer test')
#     timer = HashedWheelTimer()
#     barrier = CountDownLatch(1)
#     # timeout = timer.newTimeout(barrier.count_down())
#     pass


class ResTimerTest(unittest.TestCase):
    # def setUp(self) -> None:
    #     return super().setUp()

    def testRedis(self):
        print("================ Timer Redis ================")
        client = get_redis()
        # import ipdb ; ipdb.set_trace()

    def testGetSchedule(self):
        schedule = RedTimer().schedule
        print(schedule)


def main():
    print("main")


if __name__ == "__main__":
    # main()

    unittest.main()
