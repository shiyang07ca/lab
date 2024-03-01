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

  @Test
  public void initRedisEntryTest() {
    // 每 3 分钟触发一次
    String cronExp = "0 0/3 * * * ?";

    String jobName = "job1";
    String jobKey = String.format("timer::%s", jobName);

    String TIMER_SCHEDULE_KEY = "timer::schedule";

    ScheduleDto scheduleDto =
        ScheduleDto.builder()
            .type("crontab")
            .second("0")
            .minute("0/3")
            .hour("*")
            .dayOfMonth("*")
            .month("*")
            .dayOfWeek("?")
            .build();
    JobDefinitionDto defDto =
        JobDefinitionDto.builder().name(jobName).params("test").schedule(scheduleDto).build();
    JobMetaDto metaDto =
        JobMetaDto.builder().lastRunAt(ZonedDateTime.of(2010, 1, 1, 0, 0, 0, 0, zoneId)).build();

    //    JobDto jobDto = JobDto.builder().definition(defDto).meta(metaDto).build();

    RMap<String, Object> map = r.getMap(jobKey);
    map.put("definition", defDto);
    map.put("meta", metaDto);
    //    System.out.println("map: " + map.get("definition"));
    //    System.out.println("=======================");
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

    RScoredSortedSet<String> set = r.getScoredSortedSet("mySortedSet");
    set.add(timestamp1, "t1");
    set.add(timestamp2, "t2");
    List<String> jobNames = (List<String>) set.valueRange(0, true, nowTimestamp, true);
    for (String string : jobNames) {
      System.out.println("string: " + string + '\n');
    }
  }

  @Test
  public void testGetTimerSchedule() {
    new RedisTimerImpl().getSchedule();
  }
}
