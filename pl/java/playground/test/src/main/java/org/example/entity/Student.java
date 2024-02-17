package org.example.entity;

import lombok.Data;

@Data
public class Student {
  int sid; // 名称最好和数据库字段名称保持一致，不然可能会映射失败导致查询结果丢失
  String name;
  String sex;
}
