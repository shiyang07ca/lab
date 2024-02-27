import static com.cronutils.model.field.expression.FieldExpressionFactory.*;

import com.cronutils.builder.CronBuilder;
import com.cronutils.model.Cron;
import com.cronutils.model.CronType;
import com.cronutils.model.definition.CronDefinitionBuilder;
import com.cronutils.model.field.CronFieldName;
import org.example.timer.Crontab;
import org.example.timer.exception.CronParseException;
import org.junit.Assert;
import org.junit.Test;

public class CrontabTest {
  @Test
  public void testCronAsString() {
    Cron cron =
        CronBuilder.cron(CronDefinitionBuilder.instanceDefinitionFor(CronType.QUARTZ))
            .withYear(always())
            .withDoW(questionMark())
            .withMonth(always())
            .withDoM(always())
            .withHour(always())
            .withMinute(every(5))
            .withSecond(on(0))
            .instance();
    // Obtain the string expression
    String cronAsString = cron.asString();

    // 0 */5 * * * ? *  Every five minutes(once every 5 minutes)
    Assert.assertEquals("0 */5 * * * ? *", cronAsString);
  }

  @Test
  public void testCronParse() throws CronParseException {
    String strCrontab = "0 1 2 3 * ? *";

    Cron depCron = Crontab.parse2Cron(strCrontab);
    Assert.assertEquals("0", depCron.retrieve(CronFieldName.SECOND).getExpression().asString());
    Assert.assertEquals("1", depCron.retrieve(CronFieldName.MINUTE).getExpression().asString());
    Assert.assertEquals("2", depCron.retrieve(CronFieldName.HOUR).getExpression().asString());
    Assert.assertEquals(
        "3", depCron.retrieve(CronFieldName.DAY_OF_MONTH).getExpression().asString());
    Assert.assertEquals("*", depCron.retrieve(CronFieldName.MONTH).getExpression().asString());
    Assert.assertEquals("*", depCron.retrieve(CronFieldName.YEAR).getExpression().asString());
  }

  @Test
  public void testCronIsValid() {
    String strCrontab = "0 1 2 3 * ? *";
    Assert.assertTrue(Crontab.isValidExpression(strCrontab));

    strCrontab = "0 1 2 3 4 5 6";
    Assert.assertFalse(Crontab.isValidExpression(strCrontab));
  }
}
