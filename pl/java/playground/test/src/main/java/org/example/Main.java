package org.example;

import java.beans.*;
import java.lang.management.ManagementFactory;

class Person {
  private String name;
  private int age;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }
}

public class Main {
  public static void main(String[] args) throws Exception {
    // Press ⌥⏎ with your caret at the highlighted text to see how
    // IntelliJ IDEA suggests fixing it.
    System.out.printf("Hello and welcome!");
    // Press ⇧F10 or click the green arrow button in the gutter to run the code.
    for (int i = 1; i <= 5; i++) {
      // Press ⇧F9 to start debugging your code. We have set one breakpoint
      // for you, but you can always add more by pressing ⌃F8.
      System.out.println("i = " + i);
    }

    //        testIntrospect();

    t1();
  }

  static void t1() {
    String jvmName = ManagementFactory.getRuntimeMXBean().getName();
    System.out.println("Current JVM Name: " + jvmName);

    // Extracting the PID if needed
    long pid = Long.parseLong(jvmName.split("@")[0]);
    System.out.println("Current JVM PID: " + pid);
  }

  private static void testIntrospect() throws Exception {
    BeanInfo info = Introspector.getBeanInfo(Person.class);
    for (PropertyDescriptor pd : info.getPropertyDescriptors()) {
      System.out.println(pd.getName());
      System.out.println("  " + pd.getReadMethod());
      System.out.println("  " + pd.getWriteMethod());
    }
  }
}
