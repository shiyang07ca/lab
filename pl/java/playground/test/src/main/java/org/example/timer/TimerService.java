package org.example.timer;

import org.redisson.Redisson;
import org.redisson.api.RScoredSortedSet;
import org.redisson.api.RedissonClient;
import org.redisson.config.Config;

public class TimerService {
  public static void main(String[] args) {
    TimerService s = new TimerService();
    s.start();
  }

  public void start() {
    // TODO: Init redis client
    // TODO: Get all schedule task
    // TODO: Redis lock wait
    System.out.println("start");
    // 1. Create config object
    Config config = new Config();
    config.useSingleServer().setAddress("redis://127.0.0.1:6379/0");
    RedissonClient redisson = Redisson.create(config);

    //    RScoredSortedSet<String> set = redisson.getScoredSortedSet("timer::schedule");
    RScoredSortedSet<String> set = redisson.getScoredSortedSet("tzset");
    //    RScoredSortedSet<String> set = redisson.getScoredSortedSet("mySortedSet");
    set.add(10, "1");
    set.add(20, "2");
    set.add(30, "3");

    for (String s : set) {
      System.out.println("val: " + s);
    }

    redisson.shutdown();
    System.out.println("==== done ====");
  }

  public void stop() {
    System.out.println("stop");
  }
}
