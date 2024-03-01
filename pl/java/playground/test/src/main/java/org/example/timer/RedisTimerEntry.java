package org.example.timer;

import java.time.ZonedDateTime;
import org.example.timer.dto.JobDefinitionDto;
import org.example.timer.dto.JobMetaDto;
import org.redisson.api.RMap;
import org.redisson.api.RedissonClient;

public class RedisTimerEntry {

  public String jobName;
  public JobDefinitionDto jobDef;

  public JobMetaDto jobMeta;

  public RedisTimerEntry(String jobNmae, JobDefinitionDto jobDef, JobMetaDto jobMeta) {
    this.jobDef = jobDef;
    this.jobMeta = jobMeta;
    this.jobName = jobNmae;
  }

  public static RedisTimerEntry getJobByName(String jobName) {
    RedisManager.initialize();
    RedissonClient r = RedisManager.getInstance();
    RMap<String, Object> map = r.getMap(jobName);
    return new RedisTimerEntry(
        jobName, (JobDefinitionDto) map.get("definition"), (JobMetaDto) map.get("meta"));
  }

  // 更新任务的最后一次运行时间，运行总数
  public void updateJobMeta(String jobName, ZonedDateTime lastRunAt) {
    this.jobMeta.setLastRunAt(lastRunAt);
    this.jobMeta.setTotalRunCount(this.jobMeta.getTotalRunCount() + 1);
    this.save(jobName, this.jobMeta);
  }

  public void save(String jobName, JobMetaDto jobMeta) {
    // TODO: save job definition and meta to redis entry
    // TODO: zadd job and score to redis schedule
    RedisManager.initialize();
    RedissonClient r = RedisManager.getInstance();
    RMap<String, Object> map = r.getMap(jobName);
    map.put("meta", jobMeta);
  }

  public void delete() {}
}
