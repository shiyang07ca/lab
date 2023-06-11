# Created by shiyang07ca at 2023/06/11 00:06
# https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

"""
1171. 从链表中删去总和值为零的连续节点 (Medium)
给你一个链表的头节点 `head`，请你编写代码，反复删去链表中由 **总和** 值为 `0` 的连续节点组成的序列，
直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。

你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 `ListNode` 对象序列化的表示。）

**示例 1：**

```
输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。

```

**示例 2：**

```
输入：head = [1,2,3,-3,4]
输出：[1,2,4]

```

**示例 3：**

```
输入：head = [1,2,3,-3,-2]
输出：[1]

```

**提示：**

- 给你的链表中可能有 `1` 到 `1000` 个节点。
- 对于链表中的每个节点，节点的值： `-1000 <= node.val <= 1000`.

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 链接：https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/solutions/2304678/python3javacgotypescript-yi-ti-yi-jie-qi-3vsy/
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last = {}
        s, cur = 0, dummy
        while cur:
            s += cur.val
            last[s] = cur
            cur = cur.next
        s, cur = 0, dummy
        while cur:
            s += cur.val
            cur.next = last[s].next
            cur = cur.next
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().removeZeroSumSublists(head)

    print("\noutput:", serialize(ans))
