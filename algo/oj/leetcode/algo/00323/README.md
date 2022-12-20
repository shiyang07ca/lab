323. 无向图中连通分量的数目

你有一个包含 `n` 个节点的图。给定一个整数 `n` 和一个数组 `edges` ，其中 `edges[i] = [ai, bi]` 表示图中 `ai` 和 `bi` 之间有一条边。

返回 *图中已连接分量的数目* 。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/conn1-graph.jpg)

```txt
输入: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
输出: 2
```

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/conn2-graph.jpg)

```txt
输入: n = 5, edges = [[0,1], [1,2], [2,3], [3,4]]
输出:  1
```


**提示：**

-   `1 <= n <= 2000`
-   `1 <= edges.length <= 5000`
-   `edges[i].length == 2`
-   `0 <= ai <= bi < n`
-   `ai != bi`
-   `edges` 中不会出现重复的边
