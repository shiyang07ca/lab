package org.example.timer;

import java.time.ZonedDateTime;
import org.redisson.api.RedissonClient;

public class RedisTimerImpl implements Timer {

  RedisTimerEntry JOB_ENTRY;

  private static RedissonClient getRedisClient() {
    RedisManager.initialize();
    return RedisManager.getInstance();
  }

  @Override
  public void tick() {
    RedissonClient client = RedisTimerImpl.getRedisClient();
  }

  @Override
  public void getSchedule() {
    RedissonClient client = RedisTimerImpl.getRedisClient();
    long maxDueAt = ZonedDateTime.now().toEpochSecond();
    System.out.println("maxDueAt: " + maxDueAt);
    // TODO: extract schedule key
    //    client.getScoredSortedSet("timer::schedule", );
  }

  @Override
  public void addTimeout() {}

  @Override
  public void deleteTimeout() {}
}
