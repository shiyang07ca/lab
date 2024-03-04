package org.example.timer;

import com.fasterxml.jackson.core.JsonProcessingException;
import java.util.List;

public interface Timer {
  Long tick() throws JsonProcessingException;

  List<RedisTimerEntry> getSchedule() throws JsonProcessingException;

  void addTimeout(String jobName, String cronExp);

  void deleteTimeout();
}
