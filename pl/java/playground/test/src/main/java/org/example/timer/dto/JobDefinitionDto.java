package org.example.timer.dto;

import lombok.Data;

@Data
class JobDefinitionDto {
  private String enabled = "true";

  private String name;
  private String params = "";
  private ScheduleDto schedule;
}
