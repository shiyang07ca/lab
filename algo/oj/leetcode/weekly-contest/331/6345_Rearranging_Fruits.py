"""

6345. Rearranging Fruits

You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i],basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.



Example 1:

Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
Output: 1
Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.


Example 2:

Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
Output: -1
Explanation: It can be shown that it is impossible to make both the baskets equal.


Constraints:

basket1.length == bakste2.length
1 <= basket1.length <= 105
1 <= basket1[i],basket2[i] <= 109


################################################################



6345. 重排水果

你有两个果篮，每个果篮中有 n 个水果。给你两个下标从 0 开始的整数数组 basket1 和 basket2 ，用以表示两个果篮中每个水果的成本。

你希望两个果篮相等。为此，可以根据需要多次执行下述操作：

选中两个下标 i 和 j ，并交换 basket1 中的第 i 个水果和 basket2 中的第 j 个水果。
交换的成本是 min(basket1i,basket2j) 。
根据果篮中水果的成本进行排序，如果排序后结果完全相同，则认为两个果篮相等。

返回使两个果篮相等的最小交换成本，如果无法使两个果篮相等，则返回 -1 。



示例 1：

输入：basket1 = [4,2,2,2], basket2 = [1,4,1,2]
输出：1
解释：交换 basket1 中下标为 1 的水果和 basket2 中下标为 0 的水果，交换的成本为 1 。此时，basket1 = [4,1,2,2] 且 basket2 = [2,4,1,2] 。重排两个数组，发现二者相等。


示例 2：

输入：basket1 = [2,3,4,1], basket2 = [3,2,5,1]
输出：-1
解释：可以证明无法使两个果篮相等。


提示：

basket1.length == bakste2.length
1 <= basket1.length <= 105
1 <= basket1i,basket2i <= 109



"""

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/rearranging-fruits/solution/tan-xin-gou-zao-by-endlesscheng-c2ui/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter()
        for x, y in zip(basket1, basket2):
            cnt[x] += 1
            cnt[y] -= 1
        mn = min(cnt)
        a = []
        for x, c in cnt.items():
            if c % 2:
                return -1
            a.extend([x] * (abs(c) // 2))
        a.sort()  # 也可以用快速选择
        return sum(min(x, mn * 2) for x in a[: len(a) // 2])
