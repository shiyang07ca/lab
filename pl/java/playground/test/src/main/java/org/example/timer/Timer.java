package org.example.timer;

import java.util.List;

public interface Timer {
  Long tick();

  List<RedisTimerEntry> getSchedule();

  void addTimeout(String jobName, String cronExp);

  void deleteTimeout();
}
