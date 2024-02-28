package org.example.timer.dto;

import lombok.Data;

import java.time.ZonedDateTime;

@Data
class JobMetaDto {
  private ZonedDateTime lastRunAt;
  private int totalRunCount;
}
