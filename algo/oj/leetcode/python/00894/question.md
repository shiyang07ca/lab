# [894. 所有可能的真二叉树][link] (Medium)

[link]: https://leetcode.cn/problems/all-possible-full-binary-trees/

给你一个整数 `n` ，请你找出所有可能含 `n` 个节点的 **真二叉树** ，并以列表形式返回。答案中每棵树的每
个节点都必须符合 `Node.val == 0` 。

答案的每个元素都是一棵真二叉树的根节点。你可以按 **任意顺序** 返回最终的真二叉树列表 **。**

**真二叉树** 是一类二叉树，树中每个节点恰好有 `0` 或 `2` 个子节点。

**示例 1：**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png)

```
输入：n = 7
输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null
,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

```

**示例 2：**

```
输入：n = 3
输出：[[0,0,0]]

```

**提示：**

- `1 <= n <= 20`
