package org.example.doc.dynamic;

import java.lang.annotation.Annotation;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.Method;

public class MethodAnnotations {
  public static void main(String[] args) throws Exception {
    Class<?> cls = MethodAnnotations.class;
    Method method = cls.getMethod("hello", String.class, String.class);

    Annotation[][] annts = method.getParameterAnnotations();
    for (int i = 0; i < annts.length; i++) {
      System.out.println("annotations for paramter " + (i + 1));
      Annotation[] anntArr = annts[i];
      for (Annotation annt : anntArr) {
        if (annt instanceof QueryParam qp) {
			System.out.println(qp.annotationType().getSimpleName() + ":" + qp.value());
        } else if (annt instanceof DefaultValue dv) {
			System.out.println(dv.annotationType().getSimpleName() + ":" + dv.value());
        }
      }
    }
  }

  public void hello(
      @QueryParam("action") String action, @QueryParam("sort") @DefaultValue("asc") String sort) {
    // ...
  }

  @Target(ElementType.PARAMETER)
  @Retention(RetentionPolicy.RUNTIME)
  @interface QueryParam {
    String value();
  }

  @Target(ElementType.PARAMETER)
  @Retention(RetentionPolicy.RUNTIME)
  @interface DefaultValue {
    String value() default "";
  }
}
