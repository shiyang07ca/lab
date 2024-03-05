package org.example.timer.dto;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.datatype.jsr310.ser.ZonedDateTimeSerializer;
import java.time.ZonedDateTime;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.jackson.Jacksonized;
import org.example.timer.util.ZonedDateTimeDeserializer;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Jacksonized
public class RemoteJobDto {
  //  private boolean enabled = true;

  private String name;

  private String lang = "java";

  // job 触发时间
  @JsonSerialize(using = ZonedDateTimeSerializer.class)
  @JsonDeserialize(using = ZonedDateTimeDeserializer.class)
  @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd'T'HH:mm:ss.SSSZ")
  private ZonedDateTime triggeredAt;

  // job 所属业务
  private String group = "allinone";

  // job 对应函数参数
  private String params = "";

  private ScheduleDto schedule;
}
