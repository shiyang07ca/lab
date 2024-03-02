import static org.junit.Assert.assertEquals;

import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.List;
import java.util.TimeZone;
import org.example.timer.RedisManager;
import org.example.timer.RedisTimerEntry;
import org.example.timer.RedisTimerImpl;
import org.example.timer.dto.JobDefinitionDto;
import org.example.timer.dto.JobMetaDto;
import org.example.timer.dto.ScheduleDto;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.redisson.api.RMap;
import org.redisson.api.RScoredSortedSet;
import org.redisson.api.RedissonClient;

public class UpsertRedisEntryTest {

  TimeZone original;

  ZoneId zoneId;

  RedissonClient r;

  String jobKey;

  String TIMER_SCHEDULE_KEY = "timer::schedule";

  @Before
  public void setUp() {
    original = TimeZone.getDefault();
    //    TimeZone.setDefault(TimeZone.getTimeZone("Europe/Oslo"));
    TimeZone.setDefault(TimeZone.getTimeZone("Asia/Shanghai"));
    zoneId = TimeZone.getDefault().toZoneId();

    RedisManager.initialize();
    r = RedisManager.getInstance();

    jobKey = "timer::job1";
  }

  @After
  public void tearDown() {
    TimeZone.setDefault(original);
  }

  @Test
  public void testRedisManager() {
    RedisManager.initialize();
    RedissonClient r = RedisManager.getInstance();
    RScoredSortedSet<String> set = r.getScoredSortedSet("tzset");
    set.add(10, "1");
    set.add(20, "2");
    set.add(30, "3");
    assertEquals(set.toArray(), new String[] {"1", "2", "3"});
  }

  public void initRedisEntry(String jobName, String cronExp) {
    // 每 3 分钟触发一次
    //    String cronExp = "0 0/3 * * * ?";
    //    String jobName = "job1";

    // split cron exp to field
    String[] fields = cronExp.split(" ");
    String type = fields[0];
    String second = fields[0];
    String minute = fields[1];
    String hour = fields[2];
    String dayOfMonth = fields[3];
    String month = fields[4];
    String dayOfWeek = fields[5];

    ScheduleDto scheduleDto =
        ScheduleDto.builder()
            .type(type)
            .second(second)
            .minute(minute)
            .hour(hour)
            .dayOfMonth(dayOfMonth)
            .month(month)
            .dayOfWeek(dayOfWeek)
            .build();
    JobDefinitionDto defDto =
        JobDefinitionDto.builder().name(jobName).params("test").schedule(scheduleDto).build();
    JobMetaDto metaDto =
        JobMetaDto.builder().lastRunAt(ZonedDateTime.of(2010, 1, 1, 0, 0, 0, 0, zoneId)).build();

    String jobKey = String.format("timer::%s", jobName);
    RMap<String, Object> map = r.getMap(jobKey);
    map.put("definition", defDto);
    map.put("meta", metaDto);
  }

  @Test
  public void testGetRedisEntryByName() {
    RedisTimerEntry entry = RedisTimerEntry.getJobByName(jobKey);
    assertEquals(entry.jobName, jobKey);
  }

  @Test
  public void testUpdateRedisEntry() {
    RedisTimerEntry entry = RedisTimerEntry.getJobByName(jobKey);
    entry.updateJobMeta(jobKey, ZonedDateTime.now());
    System.out.println("entry: " + entry.jobMeta);
  }

  @Test
  public void addEntry2Schedule() {
    long timestamp1 = ZonedDateTime.of(2010, 1, 1, 0, 0, 0, 0, zoneId).toEpochSecond();
    long timestamp2 = ZonedDateTime.of(2015, 12, 1, 0, 0, 0, 0, zoneId).toEpochSecond();
    long nowTimestamp = ZonedDateTime.now().toEpochSecond();

    RScoredSortedSet<String> set = r.getScoredSortedSet("timer::schedule");
    set.add(timestamp1, "timer::job1");
    set.add(timestamp2, "timer::job2");
    List<String> jobNames = (List<String>) set.valueRange(0, true, nowTimestamp, true);
    //    for (String string : jobNames) {
    //      System.out.println("string: " + string + '\n');
    //    }
    assertEquals(set.toArray(), new String[] {"timer::job1", "timer::job2"});
  }

  @Test
  public void initRedisJobs() {
    initRedisEntry("job1", "0 0/3 * * * ?");
    initRedisEntry("job2", "0 0 12 ? * WED");
  }

  @Test
  public void testGetTimerSchedule() {
    new RedisTimerImpl().getSchedule();
  }

  @Test
  public void testTimerServiceTick() {
    new RedisTimerImpl().tick();
  }

  @Test
  public void testTimerAddTimeout() {
    // TODO: implement
    new RedisTimerImpl().addTimeout(jobKey, "0 0/3 * * * ?");
  }

  @Test
  public void testUpdateJobSchedule() {
    RedisTimerEntry entry = RedisTimerEntry.getJobByName(jobKey);
    ZonedDateTime time = ZonedDateTime.of(2018, 10, 1, 0, 0, 0, 0, zoneId);
    entry.updateJobSchedule(jobKey, time);
  }

  @Test
  public void testEntryGetNextRunTimes() {
    RedisTimerEntry entry = RedisTimerEntry.getJobByName(jobKey);
    ZonedDateTime start = ZonedDateTime.of(2018, 10, 1, 0, 0, 0, 0, zoneId);
    List<ZonedDateTime> nextRunTimes = entry.getNextRunTimes(start);
    System.out.println("Star: " + start);
    System.out.println("Cron: " + entry.jobDef.getSchedule().getCronExp());
    System.out.println("nextRunTime: " + nextRunTimes);
  }
}
