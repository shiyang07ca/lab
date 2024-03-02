package org.example.timer;

import java.time.Duration;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import org.redisson.api.RScoredSortedSet;
import org.redisson.api.RedissonClient;

public class RedisTimerImpl implements Timer {

  // TODO: modify this parameter
  // default max interval is 500ms
  Long maxInterval = 2000L;

  private static RedissonClient getRedisClient() {
    RedisManager.initialize();
    return RedisManager.getInstance();
  }

  @Override
  public Long tick() {
    List<Long> nextTimes = new ArrayList<>(List.of(maxInterval));

    List<RedisTimerEntry> entries = getSchedule();
    for (RedisTimerEntry entry : entries) {
      ZonedDateTime dueAt = entry.dueAt();
      System.out.println("entry: " + entry.jobName);
      //      System.out.println("dueAt: " + dueAt);

      ZonedDateTime now = ZonedDateTime.now().plusNanos(10);
      if (now.isAfter(dueAt)) {
        // TODO: send job to pubsub
        // TODO: logging
        entry.apply();
        entry.updateJobMeta(entry.jobName, now);
        entry.updateJobSchedule(entry.jobName, now);
      } else {
        long delta = Duration.between(now, dueAt).toMillis();
        nextTimes.add(Math.max(delta, 0L));
      }
    }
    return Collections.min(nextTimes);
  }

  @Override
  public List<RedisTimerEntry> getSchedule() {
    List<RedisTimerEntry> entries = new ArrayList<>();
    // TODO: extract schedule key
    RedissonClient r = RedisTimerImpl.getRedisClient();
    RScoredSortedSet<String> set = r.getScoredSortedSet("timer::schedule");
    List<String> jobKeys =
        (List<String>) set.valueRange(0, true, ZonedDateTime.now().toEpochSecond(), true);
    for (String jobKey : jobKeys) {
      entries.add(RedisTimerEntry.getJobByName(jobKey));
    }
    return entries;
    // TODO: prefetch 1 job by zrangebyscore for check due time
  }

  @Override
  public void addTimeout(String jobName, String cronExp) {
    try {
      CronExpression expression = new CronExpression(cronExp);
    } catch (Exception e) {
      // TODO: logging
      e.printStackTrace();
    }
  }

  @Override
  public void deleteTimeout() {}
}
