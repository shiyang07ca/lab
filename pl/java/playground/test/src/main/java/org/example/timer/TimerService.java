package org.example.timer;

public class TimerService {
  public static void main(String[] args) {
    TimerService s = new TimerService();
    s.start();
  }

  public void start() {
    // TODO: Init redis client
    // TODO: Get all schedule task
    // TODO: Redis lock wait
    // TODO: prefix key with biz name
    System.out.println("start");

    RedisTimerImpl service = new RedisTimerImpl();
    while (true) {
      service.tick();
      break;
    }

    System.out.println("==== done ====");
  }

  public void stop() {
    System.out.println("stop");
  }
}
