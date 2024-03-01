package org.example.timer.dto;

import lombok.Builder;
import lombok.Data;
import lombok.extern.jackson.Jacksonized;

@Data
@Builder
@Jacksonized
public class ScheduleDto {
  private String type;
  private String second;
  private String minute;
  private String hour;
  private String dayOfMonth;
  private String month;
  private String dayOfWeek;
}
