# Created by shiyang07ca at 2023/08/12 00:22
# leetgo: dev
# https://leetcode.cn/problems/merge-k-sorted-lists/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = cur = ListNode()
        n = len(lists)
        if n == 0 or n == 1 and lists[0] is None:
            return None

        h = []
        for l in lists:
            while l:
                heappush(h, l.val)
                l = l.next
        while h:
            v = heappop(h)
            cur.next = ListNode(v)
            cur = cur.next

        return ans.next


# @lc code=end

if __name__ == "__main__":
    lists: List[ListNode] = deserialize("List[ListNode]", read_line())
    ans = Solution().mergeKLists(lists)

    print("\noutput:", serialize(ans))
