package org.example.doc;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class OptionalTest {
  public static <T> void main(String[] args) {
    Optional<T> optional = Optional.empty();
    //    Optional<T> optional2 = Optional.of(objectT);
    System.out.println(optional);

    Map<String, Object> map = new HashMap<>();
    map.put("foo", "bar");
    String value = Optional.ofNullable(map.get("foo")).map(Object::toString).orElse("helloworld");
    System.out.println(value);
  }
}
