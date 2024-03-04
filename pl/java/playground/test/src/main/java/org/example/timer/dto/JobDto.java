package org.example.timer.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.extern.jackson.Jacksonized;

@Data
@Builder
@Jacksonized
@AllArgsConstructor
public class JobDto {
  private JobDefinitionDto definition;
  private JobMetaDto meta;
}
