package org.example.timer;

public interface Timer {
  void tick();

  void getSchedule();

  void addTimeout();

  void deleteTimeout();
}
