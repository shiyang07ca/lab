package org.example.dynamic.c86.dynamic.c86;

import shuo.laoma.dynamic.c86.dynamic.c85.SimpleInject;

public class ServiceA {

  @SimpleInject ServiceB b;

  public void callB() {
    b.action();
  }

  public ServiceB getB() {
    return b;
  }
}
