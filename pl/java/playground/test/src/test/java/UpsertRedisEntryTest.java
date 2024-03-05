import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.lettuce.core.*;
import io.lettuce.core.api.sync.RedisCommands;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.List;
import java.util.TimeZone;
import java.util.stream.Collectors;
import org.example.timer.RedisManager;
import org.example.timer.RedisTimerEntry;
import org.example.timer.RedisTimerImpl;
import org.example.timer.dto.JobDefinitionDto;
import org.example.timer.dto.JobMetaDto;
import org.example.timer.dto.ScheduleDto;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.redisson.api.*;

public class UpsertRedisEntryTest {

  TimeZone original;

  ZoneId zoneId;

  RedisClient r;

  String jobKey;

  String TIMER_SCHEDULE_KEY = "timer::schedule";

  @Before
  public void setUp() {
    original = TimeZone.getDefault();
    TimeZone.setDefault(TimeZone.getTimeZone("Asia/Shanghai"));
    zoneId = TimeZone.getDefault().toZoneId();

    r = RedisManager.getInstance();

    jobKey = String.format("timer::%s", "job1");
  }

  @After
  public void tearDown() {
    TimeZone.setDefault(original);
  }

  @Test
  public void testRedisManager() {
    RedisCommands<String, String> commands = r.connect().sync();
    String key = "tzset";
    commands.zadd(key, 10, "1");
    commands.zadd(key, 20, "2");
    commands.zadd(key, 30, "3");
    List<String> allMembers = commands.zrange(key, 0, -1);
    assertEquals(allMembers.toArray(), new String[] {"1", "2", "3"});
  }

  public void initRedisEntry(String jobName, String cronExp) throws JsonProcessingException {
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

    String key = String.format("timer::%s", jobName);
    RedisCommands<String, String> commands = r.connect().sync();

    ObjectMapper objectMapper = new ObjectMapper();
    String defStr = objectMapper.writeValueAsString(defDto);
    String metaStr = objectMapper.writeValueAsString(metaDto);
    commands.hset(key, "definition", defStr);
    commands.hset(key, "meta", metaStr);
  }

  @Test
  public void testGetRedisEntryByName() throws JsonProcessingException {
    RedisTimerEntry entry = new RedisTimerEntry(jobKey);
    assertEquals(entry.jobName, jobKey);
  }

  @Test
  public void testUpdateRedisEntry() throws JsonProcessingException {
    RedisTimerEntry before = new RedisTimerEntry(jobKey);

    RedisTimerEntry after = new RedisTimerEntry(jobKey);
    after.updateJobMeta(jobKey, ZonedDateTime.now());

    assertTrue(after.jobMeta.getLastRunAt().isAfter(before.jobMeta.getLastRunAt()));
    assertEquals(before.jobMeta.getTotalRunCount() + 1, after.jobMeta.getTotalRunCount());
  }

  @Test
  public void testUpdateJobSchedule() throws JsonProcessingException {
    RedisTimerEntry before = new RedisTimerEntry(jobKey);
    ZonedDateTime time = ZonedDateTime.of(2018, 10, 1, 0, 0, 0, 0, zoneId);
    //    ZonedDateTime time = ZonedDateTime.now();
    before.updateJobSchedule(jobKey, time);

    List<RedisTimerEntry> entries = new RedisTimerImpl().getSchedule();
    System.out.println(entries.stream().map(e -> e.jobName).collect(Collectors.toList()));
  }

  @Test
  public void initRedisJobs() throws JsonProcessingException {
    initRedisEntry("job1", "0 0/3 * * * ?");
    initRedisEntry("job2", "0 0 12 ? * WED");
  }

  @Test
  public void testGetTimerSchedule() throws JsonProcessingException {
    long timestamp1 = ZonedDateTime.of(2010, 1, 1, 0, 0, 0, 0, zoneId).toEpochSecond();
    long timestamp2 = ZonedDateTime.of(2015, 12, 1, 0, 0, 0, 0, zoneId).toEpochSecond();

    String key = "timer::schedule";
    RedisCommands<String, String> commands = r.connect().sync();
    commands.zadd(key, timestamp1, "timer::job1");
    commands.zadd(key, timestamp2, "timer::job2");

    List<RedisTimerEntry> entries = new RedisTimerImpl().getSchedule();
    assertEquals(
        new String[] {"timer::job1", "timer::job2"},
        entries.stream().map(e -> e.jobName).collect(Collectors.toList()).toArray());
  }

  //  @Test
  //  public void testTimerServiceTick() {
  //    new RedisTimerImpl().tick();
  //  }

  @Test
  public void testRedisStreamPubMsg() {
    RedisCommands<String, String> commands = r.connect().sync();

    //    String key = "timer::allinone::stream";
    String key = "myStream";
    String groupName = "myGroup";

    // lettuce check consumer group is exist

    // 使用Lettuce提供的方法来获取stream的信息
    // 直接调用xinfoGroups获取消费者组列表
    //    List<ConsumerGroup> groups = commands.xinfoGroups(key);
    //    boolean groupExists = groups.stream().anyMatch(group ->
    // groupName.equals(group.getName()));
    //    System.out.println("groupExists: " + groupExists);

    //    commands.xgroupCreate(
    //            XReadArgs.StreamOffset.from(key, "$"), groupName,
    // XGroupCreateArgs.Builder.mkstream());
    //    Map<String, String> messageBody = new HashMap<>();
    //    messageBody.put("speed", "15");
    //    messageBody.put("direction", "270");
    //    commands.xadd(key, messageBody);
  }

  @Test
  public void testRedisReadMsg1() throws InterruptedException {
    //    CountDownLatch latch = new CountDownLatch(1);

    RedisCommands<String, String> commands = r.connect().sync();
    String key = "myStream";
    String groupName = "myGroup";
    //    List<StreamMessage<String, String>> messages =
    //        commands.xreadgroup(
    //            Consumer.from(group, "consumer1"), XReadArgs.StreamOffset.lastConsumed(key));
    //

    List<StreamMessage<String, String>> messages =
        commands.xreadgroup(
            Consumer.from(groupName, "consumer_1"),
            XReadArgs.Builder.block(5000).count(2),
            XReadArgs.StreamOffset.lastConsumed(key));

    if (!messages.isEmpty()) {
      for (StreamMessage<String, String> message : messages) {
        System.out.println("==================Message ID: " + message.getId());
        System.out.println("==================Message Body: " + message.getBody());
        // Confirm that the message has been processed using XACK
        //        commands.xack(key, groupName, message.getId());
        break;
      }
    }

    //    latch.await();
  }

  //
  //  @Test
  //  public void testRedisReadMsg2() throws InterruptedException {
  //    CountDownLatch latch = new CountDownLatch(1);
  //
  //    RTopic topic = r.getTopic("myTopic");
  //
  //    // 添加消息监听器
  //    int registrationId =
  //        topic.addListener(
  //            String.class,
  //            new MessageListener<String>() {
  //              @Override
  //              public void onMessage(CharSequence channel, String msg) {
  //                System.out.println("接收到消息: " + msg);
  //              }
  //            });
  //
  //    latch.await();
  //  }
  //
  //  @Test
  //  public void testTimerAddTimeout() {
  //    // TODO: implement
  //    new RedisTimerImpl().addTimeout(jobKey, "0 0/3 * * * ?");
  //  }
  //

  @Test
  public void testEntryGetNextRunTimes() throws JsonProcessingException {
    RedisTimerEntry entry = new RedisTimerEntry(jobKey);
    ZonedDateTime start = ZonedDateTime.of(2018, 10, 1, 0, 0, 0, 0, zoneId);
    List<ZonedDateTime> nextRunTimes = entry.getNextRunTimes(start);
    System.out.println("Star: " + start);
    System.out.println("Cron: " + entry.jobDef.getSchedule().getCronExp());
    System.out.println("nextRunTime: " + nextRunTimes);
  }
}
