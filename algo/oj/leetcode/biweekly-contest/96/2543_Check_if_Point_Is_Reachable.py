"""

2543. Check if Point Is Reachable

There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point (targetX, targetY) using a finite number of steps.

In one step, you can move from point (x, y) to any one of the following points:

(x, y - x)
(x - y, y)
(2 * x, y)
(x, 2 * y)
Given two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, return true if you can reach the point from (1, 1) using some number of steps, and false otherwise.



Example 1:

Input: targetX = 6, targetY = 9
Output: false
Explanation: It is impossible to reach (6,9) from (1,1) using any sequence of moves, so false is returned.


Example 2:

Input: targetX = 4, targetY = 7
Output: true
Explanation: You can follow the path (1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7).


Constraints:

1 <= targetX, targetY <= 109

"""

"""

# TODO

2543. 判断一个点是否可以到达

给你一个无穷大的网格图。一开始你在 (1, 1) ，你需要通过有限步移动到达点 (targetX, targetY) 。

每一步 ，你可以从点 (x, y) 移动到以下点之一：

(x, y - x)
(x - y, y)
(2 * x, y)
(x, 2 * y)
给你两个整数 targetX 和 targetY ，分别表示你最后需要到达点的 X 和 Y 坐标。如果你可以从 (1, 1) 出发到达这个点，请你返回true ，否则返回 false 。



示例 1：

输入：targetX = 6, targetY = 9
输出：false
解释：没法从 (1,1) 出发到达 (6,9) ，所以返回 false 。


示例 2：

输入：targetX = 4, targetY = 7
输出：true
解释：你可以按照以下路径到达：(1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7) 。


提示：

1 <= targetX, targetY <= 109


"""

"""
比赛时的思路

(x, y - x)  =>  (x, x + y)
(x - y, y)  =>  (x + y, y)
GCD 不变

(2 * x, y)  =>  (x / 2, y)
(x, 2 * y)  =>  (x, y / 2)
GCD * 2^k

赛后的一些补充

构造一条 (1,1) 到 (x,y) 的路径
从终点出发

原则：GCD 前两个操作不变 后两个操作可以减半
和 2 有关 => 和奇偶性有关

构造方法：
1. 如果 x 和 y 只要有偶数，就把偶数减半
2. 如果都是奇数， x < y  -> x < (x + y) / 2
   为了让 y 变得更小 y -> (x + y) / 2
3. x = y 且都为奇数是， 无法修改，循环体制
4. 此时如果 x = y = 1 找到起点

"""

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        g = gcd(targetX, targetY)
        return (g & (g - 1)) == 0  # 判断是否是 2 的幂次
