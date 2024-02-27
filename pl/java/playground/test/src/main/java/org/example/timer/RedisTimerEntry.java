package org.example.timer;

import java.time.ZonedDateTime;

public class RedisTimerEntry {
  boolean due(ZonedDateTime now) {
    return true;
  }

  void saveJobEntry(String jobName) {}

  void deleteJobEntry(String jobName) {}
}
