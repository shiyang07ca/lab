package org.example.doc;

import java.lang.annotation.*;
import java.lang.reflect.Method;

//interface Annotation {
//    boolean equals(Object obj);
//
//    int hashCode();
//
//    String toString();
//
//    //返回真正的注解类型
//    Class<? extends Annotation> annotationType();
//}


public class MethodAnnotations {
    public static void main(String[] args) throws Exception {
        Class<?> cls = MethodAnnotations.class;
        Method method = cls.getMethod("hello",
                String.class, String.class);
        Annotation[][] annts = method.getParameterAnnotations();
        for (int i = 0; i < annts.length; i++) {
            System.out.println("annotations for paramter " + (i + 1));
            Annotation[] anntArr = annts[i];
            for (Annotation annt : anntArr) {
                if (annt instanceof QueryParam) {
                    QueryParam qp = (QueryParam) annt;
                    System.out.println(qp.annotationType()
                            .getSimpleName() + ":" + qp.value());
                } else if (annt instanceof DefaultValue) {
                    DefaultValue dv = (DefaultValue) annt;
                    System.out.println(dv.annotationType()
                            .getSimpleName() + ":" + dv.value());
                }
            }
        }
    }

    public void hello(@QueryParam("action") String action,
                      @QueryParam("sort") @DefaultValue("asc") String sort) {
        //…
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
