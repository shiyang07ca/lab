package org.example.timer;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.lettuce.core.RedisClient;
import io.lettuce.core.api.sync.RedisCommands;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.example.timer.dto.JobDefinitionDto;
import org.example.timer.dto.JobMetaDto;

public class RedisTimerEntry {

  public String jobName;
  public JobDefinitionDto jobDef;
  public JobMetaDto jobMeta;

  public RedisTimerEntry(String jobName) throws JsonProcessingException {
    this.jobName = jobName;
    RedisClient r = RedisManager.getInstance();
    RedisCommands<String, String> commands = r.connect().sync();
    Map<String, String> map = commands.hgetall(jobName);
    ObjectMapper objectMapper = new ObjectMapper();

    this.jobDef = objectMapper.readValue(map.get("definition"), JobDefinitionDto.class);
    this.jobMeta = objectMapper.readValue(map.get("meta"), JobMetaDto.class);
  }

  //  public void getJobByName() throws JsonProcessingException {
  //    // TODO: encapsulate redis client
  //
  //    //    return new RedisTimerEntry(
  //    //        jobName,
  //    //        objectMapper.readValue(map.get("definition"), JobDefinitionDto.class),
  //    //        objectMapper.readValue(map.get("meta"), JobMetaDto.class));
  //    //  }
  //  }

  public ZonedDateTime dueAt() {
    ZonedDateTime lastRunAt = jobMeta.getLastRunAt();
    return new CronExpression(jobDef.getSchedule().getCronExp()).nextTimeAfter(lastRunAt);
  }

  public List<ZonedDateTime> getNextRunTimes(ZonedDateTime start) {
    int cnt = 5;
    List<ZonedDateTime> list = new ArrayList<>();
    for (int i = 0; i < cnt; i++) {
      ZonedDateTime nextRunAt =
          new CronExpression(jobDef.getSchedule().getCronExp()).nextTimeAfter(start);
      list.add(nextRunAt);
      start = nextRunAt;
    }
    return list;
  }

  // 更新任务的最后一次运行时间，运行统计
  public void updateJobMeta(String jobName, ZonedDateTime lastRunAt)
      throws JsonProcessingException {
    this.jobMeta.setLastRunAt(lastRunAt);
    this.jobMeta.setTotalRunCount(this.jobMeta.getTotalRunCount() + 1);
    this.save(jobName, this.jobMeta);
  }

  /**
   * Updates the job schedule in Redis based on the provided job name and current time.
   *
   * @param jobName the name of the job to update the schedule for
   * @param now the current time
   */
  public void updateJobSchedule(String jobName, ZonedDateTime now) {
    RedisClient r = RedisManager.getInstance();
    RedisCommands<String, String> commands = r.connect().sync();

    // TODO: extract schedule key
    String key = "timer::schedule";
    ZonedDateTime nextRunAt =
        new CronExpression(jobDef.getSchedule().getCronExp()).nextTimeAfter(now);
    commands.zadd(key, nextRunAt.toEpochSecond(), jobName);
  }

  public void save(String jobName, JobMetaDto jobMeta) throws JsonProcessingException {
    // TODO: save job definition and meta to redis entry
    // TODO: zadd job and score to redis schedule
    // TODO: encapsulate redis client
    RedisClient r = RedisManager.getInstance();
    RedisCommands<String, String> commands = r.connect().sync();

    ObjectMapper objectMapper = new ObjectMapper();
    String defStr = objectMapper.writeValueAsString(jobDef);
    String metaStr = objectMapper.writeValueAsString(jobMeta);
    commands.hset(jobName, "definition", defStr);
    commands.hset(jobName, "meta", metaStr);
  }

  // Send job data through redis pubsub
  public void apply() {
    System.out.println("================================>");
    System.out.println("Called job: " + jobName);
    System.out.println("<===============================");
  }
}
