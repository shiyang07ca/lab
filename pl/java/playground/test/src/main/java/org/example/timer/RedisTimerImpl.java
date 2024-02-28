package org.example.timer;

import java.time.ZonedDateTime;
import lombok.Data;

@Data
class ScheduleDto {
  private String type;
  private String second;
  private String minute;
  private String hour;
  private String dayOfMonth;
  private String month;
  private String dayOfWeek;
}

@Data
class JobDefinitionDto {
  private String enabled = "true";

  private String name;
  private String params = "";
  private ScheduleDto schedule;
}

@Data
class JobMetaDto {
  private ZonedDateTime lastRunAt;
  private int totalRunCount;
}

class JobMetadata {}

public class RedisTimerImpl implements Timer {

  RedisTimerEntry JOB_ENTRY;

  @Override
  public void tick() {}

  @Override
  public void getSchedule() {}

  @Override
  public void addTimeout() {}

  @Override
  public void deleteTimeout() {}
}
