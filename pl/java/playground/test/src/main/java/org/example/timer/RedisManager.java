package org.example.timer;

import io.lettuce.core.RedisClient;

public class RedisManager {
  private static RedisClient instance = RedisClient.create("redis://localhost:6379");
  ;

  //  private static StatefulRedisConnection<String, String> connection;

  private RedisManager() {}

  // 初始化Redisson客户端
  //  public static synchronized void initialize() {
  //    // TODO: Redis 配置文件
  //    // TODO: 支持多种 Redis 部署模式，单机、主从复制、集群，哨兵模式
  //
  //    if (instance == null) {
  //      Config config = new Config();
  //      config.setCodec(new JsonJacksonCodec());
  //      //      config.setCodec(new SerializationCodec());
  //      config.useSingleServer().setAddress("redis://127.0.0.1:6379/0");
  //      instance = Redisson.create(config);
  //    }
  //  }

  //  public static synchronized void initialize() {
  //    // TODO: Redis 配置文件
  //    // TODO: 支持多种 Redis 部署模式，单机、主从复制、集群，哨兵模式
  //
  //    if (instance == null) {
  //      // 创建RedisClient
  //      instance = RedisClient.create("redis://localhost:6379");
  //      // 开启连接
  //      //      connection = instance.connect();
  //      //      System.out.println("Connected to Redis");
  //    }
  //  }

  // 获取Redisson客户端实例
  public static RedisClient getInstance() {
    //    if (instance == null) {
    //      throw new IllegalStateException(
    //          "RedissonClient has not been initialized. Call initialize() first.");
    //    }
    return instance;
  }

  //  public static RedisClient getConnection() {
  //    if (connection == null) {
  //      throw new IllegalStateException(
  //          "RedissonClient has not been initialized. Call initialize() first.");
  //    }
  //    return connection;
  //  }
}
