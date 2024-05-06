package org.example.dynamic.c86;

public class SimpleStaticProxyDemo {

  public static void main(String[] args) {
    IService realService = new RealService();
    IService proxyService = new TraceProxy(realService);
    proxyService.sayHello();
  }

  static interface IService {
    public void sayHello();
  }

  static class RealService implements IService {

    @Override
    public void sayHello() {
      System.out.println("hello");
    }
  }

  static class TraceProxy implements IService {
    private IService realService;

    public TraceProxy(IService realService) {
      this.realService = realService;
    }

    @Override
    public void sayHello() {
      System.out.println("entering sayHello");
      this.realService.sayHello();
      System.out.println("leaving sayHello");
    }
  }
}
