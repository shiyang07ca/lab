package org.example.timer;

import static java.lang.Thread.sleep;

public class TimerService {
  public static void main(String[] args) throws InterruptedException {
    TimerService s = new TimerService();
    s.start();
  }

  public void start() throws InterruptedException {
    // TODO: Init redis client
    // TODO: Redis lock wait
    // TODO: prefix key with biz name
    // TODO: define exception
    System.out.println("start");

    RedisTimerImpl service = new RedisTimerImpl();
    try {
      while (true) {
        long delay = service.tick();
        sleep(delay);
        System.out.println("delay: " + delay);
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
    System.out.println("==== done ====");
  }

  public void stop() {
    System.out.println("stop");
  }
}
