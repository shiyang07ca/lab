"""

[1041] Robot Bounded In Circle


On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:


	The north direction is the positive direction of the y-axis.
	The south direction is the negative direction of the y-axis.
	The east direction is the positive direction of the x-axis.
	The west direction is the negative direction of the x-axis.


The robot can receive one of three instructions:


	"G": go straight 1 unit.
	"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
	"R": turn 90 degrees to the right (i.e., clockwise direction).


The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.


Example 1:


Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.


Example 2:


Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.


Example 3:


Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.



Constraints:


	1 <= instructions.length <= 100
	instructions[i] is 'G', 'L' or, 'R'.

################################################################

1041. 困于环中的机器人

在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。注意:

北方向 是y轴的正方向。
南方向 是y轴的负方向。
东方向 是x轴的正方向。
西方向 是x轴的负方向。
机器人可以接受下列三条指令之一：

"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。

只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。



示例 1：

输入：instructions = "GGLLGG"
输出：true
解释：机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“G”:移动一步。位置:(0,2).方向:北。
“L”:逆时针旋转90度。位置:(0,2).方向:西。
“L”:逆时针旋转90度。位置:(0,2)方向:南。
“G”:移动一步。位置:(0,1)方向:南。
“G”:移动一步。位置:(0,0)方向:南。
重复指令，机器人进入循环:(0,0)——>(0,1)——>(0,2)——>(0,1)——>(0,0)。
在此基础上，我们返回true。


示例 2：

输入：instructions = "GG"
输出：false
解释：机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“G”:移动一步。位置:(0,2).方向:北。
重复这些指示，继续朝北前进，不会进入循环。
在此基础上，返回false。


示例 3：

输入：instructions = "GL"
输出：true
解释：机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“L”:逆时针旋转90度。位置:(0,1).方向:西。
“G”:移动一步。位置:(- 1,1)方向:西。
“L”:逆时针旋转90度。位置:(- 1,1)方向:南。
“G”:移动一步。位置:(- 1,0)方向:南。
“L”:逆时针旋转90度。位置:(- 1,0)方向:东方。
“G”:移动一步。位置:(0,0)方向:东方。
“L”:逆时针旋转90度。位置:(0,0)方向:北。
重复指令，机器人进入循环:(0,0)——>(0,1)——>(- 1,1)——>(- 1,0)——>(0,0)。
在此基础上，我们返回true。


提示：

1 <= instructions.length <= 100
instructions[i] 仅包含 'G', 'L', 'R'

"""

import sys
import inspect
import os
import unittest

from itertools import *
from collections import *
from copy import *
from typing import *
from math import *

from os.path import abspath, join, dirname

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # oj
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *

"""
作者：力扣官方题解
链接：https://leetcode.cn/problems/robot-bounded-in-circle/solutions/2217873/kun-yu-huan-zhong-de-ji-qi-ren-by-leetco-kjya/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


机器人想要摆脱循环，在一串指令之后的状态，必须是不位于原点且方向朝北。

"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direcIndex = 0
        x, y = 0, 0
        for instruction in instructions:
            if instruction == "G":
                x += direc[direcIndex][0]
                y += direc[direcIndex][1]
            elif instruction == "L":
                direcIndex -= 1
                direcIndex %= 4
            else:
                direcIndex += 1
                direcIndex %= 4
        return direcIndex != 0 or (x == 0 and y == 0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            self.sl,
            None,
        )


if __name__ == "__main__":
    unittest.main()
