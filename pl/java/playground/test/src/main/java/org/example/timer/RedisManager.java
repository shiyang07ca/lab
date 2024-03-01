package org.example.timer;

import org.redisson.Redisson;
import org.redisson.api.RedissonClient;
import org.redisson.codec.JsonJacksonCodec;
import org.redisson.config.Config;

public class RedisManager {
  private static RedissonClient instance = null;

  private RedisManager() {
    // 私有构造函数，防止外部实例化
  }

  // 初始化Redisson客户端
  public static synchronized void initialize() {
    // TODO: Redis 配置文件
    // TODO: 支持多种 Redis 部署模式，单机、主从复制、集群，哨兵模式
    if (instance == null) {
      Config config = new Config();
      config.setCodec(new JsonJacksonCodec());
      //      config.setCodec(new SerializationCodec());
      config.useSingleServer().setAddress("redis://127.0.0.1:6379/0");
      instance = Redisson.create(config);
    }
  }

  // 获取Redisson客户端实例
  public static RedissonClient getInstance() {
    if (instance == null) {
      throw new IllegalStateException(
          "RedissonClient has not been initialized. Call initialize() first.");
    }
    return instance;
  }
}
