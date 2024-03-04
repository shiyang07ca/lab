package org.example.timer.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.jackson.Jacksonized;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Jacksonized
@JsonIgnoreProperties(ignoreUnknown = true)
public class ScheduleDto {
  private String type;
  private String second;
  private String minute;
  private String hour;
  private String dayOfMonth;
  private String month;
  private String dayOfWeek;

  public String getCronExp() {
    return second + " " + minute + " " + hour + " " + dayOfMonth + " " + month + " " + dayOfWeek;
  }
}
