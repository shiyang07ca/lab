package org.example.timer;

import static com.cronutils.model.CronType.QUARTZ;

import com.cronutils.model.Cron;
import com.cronutils.model.definition.CronDefinitionBuilder;
import com.cronutils.parser.CronParser;
import java.time.ZonedDateTime;
import org.example.timer.exception.CronParseException;

public class Crontab {
  private static final CronParser QUARTZ_CRON_PARSER =
      new CronParser(CronDefinitionBuilder.instanceDefinitionFor(QUARTZ));

  public static Cron parse2Cron(String cronExp) throws CronParseException {
    try {
      return QUARTZ_CRON_PARSER.parse(cronExp);
    } catch (IllegalArgumentException e) {
      throw new CronParseException(String.format("Parse corn expression: [%s] error", cronExp), e);
    }
  }

  public static boolean isValidExpression(String cronExp) {
    try {
      parse2Cron(cronExp);
    } catch (CronParseException e) {
      return false;
    }
    return true;
  }

  public static ZonedDateTime getNext(ZonedDateTime lastRunAt) {
    return lastRunAt;
  }

  public static void main(String[] args) {
    System.out.println("hello world");
  }
}
