package org.example.doc.dynamic;

public class ServiceA {

  @SimpleInject ServiceB b;

  public void callB() {
    b.action();
  }

  public ServiceB getB() {
    return b;
  }
}
