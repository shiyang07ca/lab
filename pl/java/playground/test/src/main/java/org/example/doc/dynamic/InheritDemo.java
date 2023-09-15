package org.example.doc.dynamic;

import java.lang.annotation.Inherited;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

public class InheritDemo {
  public static void main(String[] args) {
    Class<?> cls = Child.class;
    System.out.println(Child.class.isAnnotationPresent(Test.class));
  }

  @Inherited
  @Retention(RetentionPolicy.RUNTIME)
  @interface Test {}

  @Test
  static class Base {}

  static class Child extends Base {}
}
