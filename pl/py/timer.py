from datetime import datetime
from enum import Enum
import json
from typing import Deque
from collections import deque

from redis import StrictRedis

from CountDownLatch import CountDownLatch
from decoder import RedBeatJSONDecoder, RedBeatJSONEncoder, to_timestamp


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


from celery.schedules import schedule

from datetime import datetime, timedelta, tzinfo


def maybe_schedule(s: int | float | timedelta, relative: bool = False):
    """Return schedule from number, timedelta, or actual schedule."""
    if s is not None:
        if isinstance(s, (float, int)):
            s = timedelta(seconds=s)
        if isinstance(s, timedelta):
            return schedule(s, relative)
    return s


SCHEDULE_KEY_PREFIX = "timer::"

SCHEDULE_KEY = SCHEDULE_KEY_PREFIX + "schedule"


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
        self.name = name
        self.task = task
        self.args = args
        self.kwargs = kwargs if kwargs else {}
        self.options = options if options else {}
        self.schedule = maybe_schedule(schedule)
        # TODO:
        import ipdb

        ipdb.set_trace()
        self.last_run_at = self.schedule.now()
        self.total_run_count = 0

        self.enabled = enabled

    @classmethod
    def from_key(cls, key):
        with get_redis().pipeline() as pipe:
            pipe.hget(key, "definition")
            pipe.hget(key, "meta")
            definition, meta = pipe.execute()

        if not definition:
            raise KeyError(key)

        definition = json.loads(definition, cls=RedBeatJSONDecoder)
        meta = json.loads(meta, cls=RedBeatJSONDecoder)
        definition.update(meta)

        entry = cls(**definition)
        entry.last_run_at = meta["last_run_at"]

        return entry

    @property
    def score(self):
        """return UTC based UNIX timestamp"""
        return to_timestamp(self.due_at)

    @property
    def due_at(self):
        # never run => due now
        if self.last_run_at is None:
            return self.schedule.now()

        delta = self.schedule.remaining_estimate(self.last_run_at)
        # if no delta, means no more events after the last_run_at.
        if delta is None:
            return None

        # overdue => due now
        if delta.total_seconds() < 0:
            return self.schedule.now()

        return self.last_run_at + delta

    @property
    def key(self):
        return SCHEDULE_KEY_PREFIX + self.name

    def save(self):
        definition = {
            "name": self.name,
            "task": self.task,
            "args": self.args,
            "kwargs": self.kwargs,
            "options": self.options,
            "schedule": self.schedule,
            "enabled": self.enabled,
        }
        meta = {
            "last_run_at": self.last_run_at,
        }
        with get_redis().pipeline() as pipe:
            pipe.hset(
                self.key, "definition", json.dumps(definition, cls=RedBeatJSONEncoder)
            )
            pipe.hsetnx(self.key, "meta", json.dumps(meta, cls=RedBeatJSONEncoder))
            pipe.zadd(SCHEDULE_KEY, {self.key: self.score})
            pipe.execute()

        return self


# TODO: redis 分布式锁
class RedTimer:
    max_interval = 30

    schedule_dict = {
        "test_every_5_seconds": {
            "name": "test_every_5_seconds",
            "task": "test_every_5_seconds_task",
            "schedule": timedelta(minutes=30),
            "args": ["param1", "param2"],  # optional
            "kwargs": {"max_targets": 100},  # optional
            "enabled": True,  # optional
        }
    }

    def start(self):
        for name, entry in RedTimer.schedule_dict.items():
            try:
                entry = RedTimerEntry(**entry)
            except Exception as e:
                print("Add entry error", name, e)
                continue
            entry.save()
            print(f"Sotred entry: {entry}")

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
        print("================ Test Timer Redis ================")
        client = get_redis()

    def testGetSchedule(self):
        schedule = RedTimer().schedule
        # print(schedule)

    def testTimerStart(self):
        RedTimer().start()


def main():
    print("main")


if __name__ == "__main__":
    # main()

    unittest.main()
