package org.example.timer.dto;

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
public class JobDefinitionDto {

  private boolean enabled = true;
  private String name;
  // job 对应函数参数
  private String params = "";
  // job 所属业务
  private String group = "allinone";
  private ScheduleDto schedule;
}
