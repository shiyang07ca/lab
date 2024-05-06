package org.example.dynamic.c86.dynamic.c85;

public class ServiceA {

  @SimpleInject ServiceB b;

  public void callB() {
    b.action();
  }

  public ServiceB getB() {
    return b;
  }
}
