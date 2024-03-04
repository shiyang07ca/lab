// package org.example.timer.util;
//
// import com.fasterxml.jackson.annotation.PropertyAccessor;
// import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;
// import com.fasterxml.jackson.annotation.JsonInclude.Include;
// import com.fasterxml.jackson.core.type.TypeReference;
// import com.fasterxml.jackson.databind.DeserializationFeature;
// import com.fasterxml.jackson.databind.ObjectMapper;
// import com.fasterxml.jackson.databind.SerializationFeature;
// import java.io.BufferedInputStream;
// import java.io.ByteArrayOutputStream;
// import java.io.IOException;
// import java.io.InputStream;
// import java.lang.reflect.Type;
// import org.apache.commons.lang3.StringUtils;
//
//
// public class JacksonUtil {
//
//    static ObjectMapper mapper = new ObjectMapper();
//
//    public JacksonUtil() {
//    }
//
//    public static boolean isValidJsonString(String checkString) {
//        try {
//            if (StringUtils.startsWith(checkString, "{") || StringUtils.startsWith(checkString,
// "[")) {
//                ObjectMapper mapper = new ObjectMapper();
//                mapper.readTree(checkString);
//                return true;
//            }
//        } catch (Throwable var2) {
//        }
//
//        return false;
//    }
//
//    public static String toJson(Object o) {
//        try {
//            return mapper.writeValueAsString(o);
//        } catch (Throwable var2) {
//            throw var2;
//        }
//    }
//
//    public static String toJsonByField(Object o) {
//        try {
//            ObjectMapper mapper = new ObjectMapper();
//            initObjectMapper(mapper);
//            mapper.setVisibility(PropertyAccessor.ALL, Visibility.NONE);
//            mapper.setVisibility(PropertyAccessor.FIELD, Visibility.ANY);
//            return mapper.writeValueAsString(o);
//        } catch (Throwable var2) {
//            throw var2;
//        }
//    }
//
//    public static String toPrettyJson(Object o) {
//        try {
//            return mapper.writerWithDefaultPrettyPrinter().writeValueAsString(o);
//        } catch (Throwable var2) {
//            throw var2;
//        }
//    }
//
//    public static <T> T toObj(String json, Class<T> t) {
//        try {
//            return t == String.class ? json : mapper.readValue(json, t);
//        } catch (Throwable var3) {
//            throw var3;
//        }
//    }
//
//    public static <T> T toObj(String json, Type type) {
//        try {
//            return type == String.class ? json : mapper.readValue(json,
// mapper.constructType(type));
//        } catch (Throwable var3) {
//            throw var3;
//        }
//    }
//
//    public static <T> T toObj(String json, TypeReference<T> ref) {
//        try {
//            return String.class.getTypeName().equals(ref.getType().getTypeName()) ? json :
// mapper.readValue(json, ref);
//        } catch (Throwable var3) {
//            throw var3;
//        }
//    }
//
//    public static <T> T toObj(InputStream inputStream, Class<T> t) {
//        try {
//            return t == String.class ? streamToString(inputStream) : mapper.readValue(inputStream,
// t);
//        } catch (Throwable var3) {
//            throw var3;
//        }
//    }
//
//    public static <T> T toObj(InputStream inputStream, Type type) {
//        try {
//            return type == String.class ? streamToString(inputStream) :
// mapper.readValue(inputStream, mapper.constructType(type));
//        } catch (Throwable var3) {
//            throw var3;
//        }
//    }
//
//    public static <T> T toObj(InputStream inputStream, TypeReference<T> ref) {
//        try {
//            return String.class.getTypeName().equals(ref.getType().getTypeName()) ?
// streamToString(inputStream) : mapper.readValue(inputStream, ref);
//        } catch (Throwable var3) {
//            throw var3;
//        }
//    }
//
//    private static String streamToString(InputStream inputStream) {
//        BufferedInputStream bis = new BufferedInputStream(inputStream);
//        ByteArrayOutputStream buf = new ByteArrayOutputStream();
//
//        try {
//            for(int result = bis.read(); result != -1; result = bis.read()) {
//                buf.write((byte)result);
//            }
//
//            return buf.toString("UTF-8");
//        } catch (IOException var5) {
//            var5.printStackTrace();
//            return "";
//        }
//    }
//
//    private static void initObjectMapper(ObjectMapper mapper) {
//        mapper.disable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
//        mapper.disable(SerializationFeature.FAIL_ON_EMPTY_BEANS);
//        mapper.setSerializationInclusion(Include.NON_NULL);
//    }
//
//    public static ObjectMapper getMapper() {
//        return mapper;
//    }
//
//    static {
//        initObjectMapper(mapper);
//    }
// }
//
// }
