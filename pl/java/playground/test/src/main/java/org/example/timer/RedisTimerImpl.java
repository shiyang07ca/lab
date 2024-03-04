package org.example.timer;

import com.fasterxml.jackson.core.JsonProcessingException;
import io.lettuce.core.RedisClient;
import io.lettuce.core.api.sync.RedisCommands;
import java.time.Duration;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class RedisTimerImpl implements Timer {

  // TODO: modify this parameter
  // default max interval is 500ms
  Long maxInterval = 2000L;

  private static RedisClient getRedisClient() {
    return RedisManager.getInstance();
  }

  @Override
  public Long tick() throws JsonProcessingException {
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
  public List<RedisTimerEntry> getSchedule() throws JsonProcessingException {
    List<RedisTimerEntry> entries = new ArrayList<>();
    // TODO: extract schedule key
    RedisCommands<String, String> commands = RedisTimerImpl.getRedisClient().connect().sync();
    // TODO: modify this
    String key = "timer::schedule";
    List<String> jobKeys = commands.zrangebyscore(key, 0, ZonedDateTime.now().toEpochSecond());

    for (String jobKey : jobKeys) {
      // TODO:
      entries.add(new RedisTimerEntry(jobKey));
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
