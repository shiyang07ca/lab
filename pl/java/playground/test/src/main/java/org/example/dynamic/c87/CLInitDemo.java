package org.example.dynamic.c87;

public class CLInitDemo {

  public static void main(String[] args) {
    ClassLoader cl = ClassLoader.getSystemClassLoader();
    String className = CLInitDemo.class.getName() + "$Hello";
    try {
      //			Class<?> cls = cl.loadClass(className);
      Class<?> cls = Class.forName(className);
    } catch (ClassNotFoundException e) {
      e.printStackTrace();
    }
  }
  ;

  public static class Hello {
    static {
      System.out.println("hello");
    }
  }
}
