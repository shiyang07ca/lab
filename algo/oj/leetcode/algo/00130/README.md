## 题目

[130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)

---

给你一个 `m x n` 的矩阵 `board` ，由若干字符 `'X'` 和 `'O'` ，找到所有被 `'X'` 围绕的区域，并将这些区域里所有的 `'O'` 用 `'X'` 填充。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)
```txt
输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
```

**示例 2：**

```txt
输入：board = [["X"]]
输出：[["X"]]
```


**提示：**

-   `m == board.length`
-   `n == board[i].length`
-   `1 <= m, n <= 200`
-   `board[i][j]` 为 `'X'` 或 `'O'`



## 解题

### 方法一：

#### 思路



#### 代码

```python3
class Solution:
    def solve(self, g: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(grid), len(grid[0])

        def dfs(x, y, path):
            pass
```
