## 题目

[855. 考场就座](https://leetcode.cn/problems/exam-room/)

---

在考场里，一排有 `N` 个座位，分别编号为 `0, 1, 2, ..., N-1` 。

当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)

返回 `ExamRoom(int N)` 类，它有两个公开的函数：其中，函数 `ExamRoom.seat()` 会返回一个 `int` （整型数据），代表学生坐的位置；函数 `ExamRoom.leave(int p)` 代表坐在座位 `p` 上的学生现在离开了考场。每次调用 `ExamRoom.leave(p)` 时都保证有学生坐在座位 `p` 上。



**示例：**

```txt
输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
输出：[null,0,9,4,2,null,5]
解释：
ExamRoom(10) -> null
seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
seat() -> 9，学生最后坐在 9 号座位上。
seat() -> 4，学生最后坐在 4 号座位上。
seat() -> 2，学生最后坐在 2 号座位上。
leave(4) -> null
seat() -> 5，学生最后坐在 5 号座位上。
```


**提示：**

1.  `1 <= N <= 10^9`
2.  在所有的测试样例中 `ExamRoom.seat()` 和 `ExamRoom.leave()` 最多被调用 `10^4` 次。
3.  保证在调用 `ExamRoom.leave(p)` 时有学生正坐在座位 `p` 上。



## 解题

### 方法一：

#### 思路



#### 代码

```python3
from sortedcontainers import SortedList


class ExamRoom:

    def __init__(self, n: int):
        def dist(x):
            l, r = x
            return r - l - 1 if l == -1 or r == n else (r - l) >> 1

        self.n = n
        self.ts = SortedList(key=lambda x: (-dist(x), x[0]))
        self.left = {}
        self.right = {}
        self.add((-1, n))

    def seat(self) -> int:
        s = self.ts[0]
        p = (s[0] + s[1]) >> 1
        if s[0] == -1:
            p = 0
        elif s[1] == self.n:
            p = self.n - 1
        self.delete(s)
        self.add((s[0], p))
        self.add((p, s[1]))
        return p

    def leave(self, p: int) -> None:
        l, r = self.left[p], self.right[p]
        self.delete((l, p))
        self.delete((p, r))
        self.add((l, r))

    def add(self, s):
        self.ts.add(s)
        self.left[s[1]] = s[0]
        self.right[s[0]] = s[1]

    def delete(self, s):
        self.ts.remove(s)
        self.left.pop(s[1])
        self.right.pop(s[0])


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

# 作者：lcbin
# 链接：https://leetcode.cn/problems/exam-room/solution/by-lcbin-tstp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
