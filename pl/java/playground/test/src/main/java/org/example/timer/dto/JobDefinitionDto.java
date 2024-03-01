package org.example.timer.dto;

import lombok.Builder;
import lombok.Data;
import lombok.extern.jackson.Jacksonized;

@Data
@Builder
@Jacksonized
public class JobDefinitionDto {
  private boolean enabled = true;

  private String name;

  private String params = "";

  private ScheduleDto schedule;
}
