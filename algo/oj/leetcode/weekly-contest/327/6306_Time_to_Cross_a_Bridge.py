"""
6306. Time to Cross a Bridge

There are k workers who want to move n boxes from an old warehouse to a new one. You are given the two integers n and k, and a 2D integer array time of size k x 4 where time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi].

The warehouses are separated by a river and connected by a bridge. The old warehouse is on the right bank of the river, and the new warehouse is on the left bank of the river. Initially, all k workers are waiting on the left side of the bridge. To move the boxes, the ith worker (0-indexed) can :

Cross the bridge from the left bank (new warehouse) to the right bank (old warehouse) in leftToRighti minutes.
Pick a box from the old warehouse and return to the bridge in pickOldi minutes. Different workers can pick up their boxes simultaneously.
Cross the bridge from the right bank (old warehouse) to the left bank (new warehouse) in rightToLefti minutes.
Put the box in the new warehouse and return to the bridge in putNewi minutes. Different workers can put their boxes simultaneously.
A worker i is less efficient than a worker j if either condition is met:

leftToRighti + rightToLefti > leftToRightj + rightToLeftj
leftToRighti + rightToLefti == leftToRightj + rightToLeftj and i > j
The following rules regulate the movement of the workers through the bridge :

If a worker x reaches the bridge while another worker y is crossing the bridge, x waits at their side of the bridge.
If the bridge is free, the worker waiting on the right side of the bridge gets to cross the bridge. If more than one worker is waiting on the right side, the one with the lowest efficiency crosses first.
If the bridge is free and no worker is waiting on the right side, and at least one box remains at the old warehouse, the worker on the left side of the river gets to cross the bridge. If more than one worker is waiting on the left side, the one with the lowest efficiency crosses first.
Return the instance of time at which the last worker reaches the left bank of the river after all n boxes have been put in the new warehouse.


Example 1:

Input: n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
Output: 6
Explanation:
From 0 to 1: worker 2 crosses the bridge from the left bank to the right bank.
From 1 to 2: worker 2 picks up a box from the old warehouse.
From 2 to 6: worker 2 crosses the bridge from the right bank to the left bank.
From 6 to 7: worker 2 puts a box at the new warehouse.
The whole process ends after 7 minutes. We return 6 because the problem asks for the instance of time at which the last worker reaches the left bank.


Example 2:

Input: n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
Output: 50
Explanation:
From 0  to 10: worker 1 crosses the bridge from the left bank to the right bank.
From 10 to 20: worker 1 picks up a box from the old warehouse.
From 10 to 11: worker 0 crosses the bridge from the left bank to the right bank.
From 11 to 20: worker 0 picks up a box from the old warehouse.
From 20 to 30: worker 1 crosses the bridge from the right bank to the left bank.
From 30 to 40: worker 1 puts a box at the new warehouse.
From 30 to 31: worker 0 crosses the bridge from the right bank to the left bank.
From 31 to 39: worker 0 puts a box at the new warehouse.
From 39 to 40: worker 0 crosses the bridge from the left bank to the right bank.
From 40 to 49: worker 0 picks up a box from the old warehouse.
From 49 to 50: worker 0 crosses the bridge from the right bank to the left bank.
From 50 to 58: worker 0 puts a box at the new warehouse.
The whole process ends after 58 minutes. We return 50 because the problem asks for the instance of time at which the last worker reaches the left bank.


Constraints:

1 <= n, k <= 104
time.length == k
time[i].length == 4
1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000

"""


"""
# TODO

6306. 过桥的时间

共有 k 位工人计划将 n 个箱子从旧仓库移动到新仓库。给你两个整数 n 和 k，以及一个二维整数数组 time ，数组的大小为 k x 4 ，其中 time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi] 。

一条河将两座仓库分隔，只能通过一座桥通行。旧仓库位于河的右岸，新仓库在河的左岸。开始时，所有 k 位工人都在桥的左侧等待。为了移动这些箱子，第 i 位工人（下标从 0 开始）可以：

从左岸（新仓库）跨过桥到右岸（旧仓库），用时 leftToRighti 分钟。
从旧仓库选择一个箱子，并返回到桥边，用时 pickOldi 分钟。不同工人可以同时搬起所选的箱子。
从右岸（旧仓库）跨过桥到左岸（新仓库），用时 rightToLefti 分钟。
将箱子放入新仓库，并返回到桥边，用时 putNewi 分钟。不同工人可以同时放下所选的箱子。
如果满足下面任一条件，则认为工人 i 的 效率低于 工人 j ：

leftToRighti + rightToLefti > leftToRightj + rightToLeftj
leftToRighti + rightToLefti == leftToRightj + rightToLeftj 且 i > j
工人通过桥时需要遵循以下规则：

如果工人 x 到达桥边时，工人 y 正在过桥，那么工人 x 需要在桥边等待。
如果没有正在过桥的工人，那么在桥右边等待的工人可以先过桥。如果同时有多个工人在右边等待，那么 效率最低 的工人会先过桥。
如果没有正在过桥的工人，且桥右边也没有在等待的工人，同时旧仓库还剩下至少一个箱子需要搬运，此时在桥左边的工人可以过桥。如果同时有多个工人在左边等待，那么 效率最低 的工人会先过桥。
所有 n 个盒子都需要放入新仓库，请你返回最后一个搬运箱子的工人 到达河左岸 的时间。



示例 1：

输入：n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
输出：6
解释：
从 0 到 1 ：工人 2 从左岸过桥到达右岸。
从 1 到 2 ：工人 2 从旧仓库搬起一个箱子。
从 2 到 6 ：工人 2 从右岸过桥到达左岸。
从 6 到 7 ：工人 2 将箱子放入新仓库。
整个过程在 7 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 6 。


示例 2：

输入：n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
输出：50
解释：
从 0 到 10 ：工人 1 从左岸过桥到达右岸。
从 10 到 20 ：工人 1 从旧仓库搬起一个箱子。
从 10 到 11 ：工人 0 从左岸过桥到达右岸。
从 11 到 20 ：工人 0 从旧仓库搬起一个箱子。
从 20 到 30 ：工人 1 从右岸过桥到达左岸。
从 30 到 40 ：工人 1 将箱子放入新仓库。
从 30 到 31 ：工人 0 从右岸过桥到达左岸。
从 31 到 39 ：工人 0 将箱子放入新仓库。
从 39 到 40 ：工人 0 从左岸过桥到达右岸。
从 40 到 49 ：工人 0 从旧仓库搬起一个箱子。
从 49 到 50 ：工人 0 从右岸过桥到达左岸。
从 50 到 58 ：工人 0 将箱子放入新仓库。
整个过程在 58 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 50 。


提示：

1 <= n, k <= 104
time.length == k
time[i].length == 4
1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000

"""


"""
https://leetcode.cn/problems/time-to-cross-a-bridge/solution/by-endlesscheng-nzqo/

建立 44 个堆，每个堆都记录工人下标和完成时间（到达桥的时间），这 44 个堆从左到右分别表示:

workL：新仓库正在放箱的工人；
waitL：左边等待过桥的工人；
waitR：右边等待过桥的工人；
workR：旧仓库正在搬箱的工人。

记录当前时间 cur，不断循环直到所有箱子被搬完，每次循环：

- 把完成时间不超过 cur 的 workL 弹出，放入 waitL 中；
- 把完成时间不超过 cur 的 workR 弹出，放入 waitR 中；
- 如果 waitR 不为空，出堆，过桥，更新 cur 为过完桥的时间，然后把这个工人放入 workL 中（记录完成时间）；
- 否则如果 waitL 不为空，出堆，过桥，更新 cur 为过完桥的时间，然后把这个工人放入
workR 中（记录完成时间），同时把 n 减一；
- 否则说明 cur 过小，找个最小的放箱/搬箱完成时间来更新 cur。
- 循环结束后，不断弹出 workR，最后一个弹出的工人的过完桥的时间即为答案。

代码实现时，也可以预先把 time 排序，这样只看下标就知道效率了


"""


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        time.sort(key=lambda t: t[0] + t[2])  # 稳定排序
        cur = 0
        workL, waitL, waitR, workR = (
            [],
            [[-i, 0] for i in range(k - 1, -1, -1)],
            [],
            [],
        )  # 下标越大效率越低
        while n:
            while workL and workL[0][0] <= cur:
                p = heappop(workL)
                p[0], p[1] = p[1], p[0]
                heappush(waitL, p)  # 左边完成放箱
            while workR and workR[0][0] <= cur:
                p = heappop(workR)
                p[0], p[1] = p[1], p[0]
                heappush(waitR, p)  # 右边完成搬箱
            if waitR and waitR[0][1] <= cur:  # 右边过桥
                p = heappop(waitR)
                cur += time[-p[0]][2]
                p[1] = p[0]
                p[0] = cur + time[-p[0]][3]
                heappush(workL, p)  # 放箱
            elif waitL and waitL[0][1] <= cur:  # 左边过桥
                p = heappop(waitL)
                cur += time[-p[0]][0]
                p[1] = p[0]
                p[0] = cur + time[-p[0]][1]
                heappush(workR, p)  # 搬箱
                n -= 1
            elif len(workL) == 0:
                cur = workR[0][0]  # cur 过小，找个最小的放箱/搬箱完成时间来更新 cur
            elif len(workR) == 0:
                cur = workL[0][0]
            else:
                cur = min(workL[0][0], workR[0][0])
        while workR:
            t, i = heappop(workR)  # 右边完成搬箱
            cur = max(t, cur) + time[-i][2]  # 过桥
        return cur  # 最后一个过桥的时间
