"""

6259. Design Memory Allocator
You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.

You have a memory allocator with the following functionalities:

Allocate a block of size consecutive free memory units and assign it the id mID.
Free all memory units with the given id mID.
Note that:

Multiple blocks can be allocated to the same mID.
You should free all the memory units with mID, even if they were allocated in different blocks.
Implement the Allocator class:

Allocator(int n) Initializes an Allocator object with a memory array of size n.
int allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.
int free(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.


Example 1:

Input
["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate", "free"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
Output
[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]

Explanation
Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free.
loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
loc.allocate(1, 2); // The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
loc.allocate(1, 3); // The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
loc.free(2); // Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
loc.allocate(3, 4); // The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
loc.allocate(1, 1); // The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
loc.allocate(1, 1); // The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
loc.free(1); // Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
loc.allocate(10, 2); // We can not find any free block with 10 consecutive free memory units, so we return -1.
loc.free(7); // Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.


Constraints:

1 <= n, size, mID <= 1000
At most 1000 calls will be made to allocate and free.


################################################################

6259. 设计内存分配器
给你一个整数 n ，表示下标从 0 开始的内存数组的大小。所有内存单元开始都是空闲的。

请你设计一个具备以下功能的内存分配器：

分配 一块大小为 size 的连续空闲内存单元并赋 id mID 。
释放 给定 id mID 对应的所有内存单元。
注意：

多个块可以被分配到同一个 mID 。
你必须释放 mID 对应的所有内存单元，即便这些内存单元被分配在不同的块中。
实现 Allocator 类：

Allocator(int n) 使用一个大小为 n 的内存数组初始化 Allocator 对象。
int allocate(int size, int mID) 找出大小为 size 个连续空闲内存单元且位于  最左侧 的块，分配并赋 id mID 。返回块的第一个下标。如果不存在这样的块，返回 -1 。
int free(int mID) 释放 id mID 对应的所有内存单元。返回释放的内存单元数目。


示例：

输入
["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate", "free"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
输出
[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]

解释
Allocator loc = new Allocator(10); // 初始化一个大小为 10 的内存数组，所有内存单元都是空闲的。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 0 。内存数组变为 [1, , , , , , , , , ]。返回 0 。
loc.allocate(1, 2); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,2, , , , , , , , ]。返回 1 。
loc.allocate(1, 3); // 最左侧的块的第一个下标是 2 。内存数组变为 [1,2,3, , , , , , , ]。返回 2 。
loc.free(2); // 释放 mID 为 2 的所有内存单元。内存数组变为 [1, ,3, , , , , , , ] 。返回 1 ，因为只有 1 个 mID 为 2 的内存单元。
loc.allocate(3, 4); // 最左侧的块的第一个下标是 3 。内存数组变为 [1, ,3,4,4,4, , , , ]。返回 3 。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,1,3,4,4,4, , , , ]。返回 1 。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 6 。内存数组变为 [1,1,3,4,4,4,1, , , ]。返回 6 。
loc.free(1); // 释放 mID 为 1 的所有内存单元。内存数组变为 [ , ,3,4,4,4, , , , ] 。返回 3 ，因为有 3 个 mID 为 1 的内存单元。
loc.allocate(10, 2); // 无法找出长度为 10 个连续空闲内存单元的空闲块，所有返回 -1 。
loc.free(7); // 释放 mID 为 7 的所有内存单元。内存数组保持原状，因为不存在 mID 为 7 的内存单元。返回 0 。


提示：

1 <= n, size, mID <= 1000
最多调用 allocate 和 free 方法 1000 次

"""


class Allocator:
    def __init__(self, n: int):
        self.m = [None] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        i = 0
        while i < self.n:
            for j in range(i, self.n):
                if self.m[j] is not None:
                    break

                if (j - i + 1) == size:
                    for k in range(i, i + size):
                        self.m[k] = mID
                    return i

            # print(i, j, self.m)
            i = j if i != j else i + 1

        return -1

    def free(self, mID: int) -> int:
        c = 0
        # print(mID, self.m)
        for i, m in enumerate(self.m):
            if m == mID:
                self.m[i] = None
                c += 1
        return c


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)


# 作者：liupengsay
# 链接：https://leetcode.cn/circle/discuss/qSroZL/view/eL8wEP/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Allocator:
    def __init__(self, n: int):
        self.lst = [-1] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        pre = 0
        for i in range(self.n):
            if self.lst[i] == -1:
                pre += 1
            else:
                pre = 0
            if pre == size:
                self.lst[i - pre + 1 : i + 1] = [mID] * size
                return i - pre + 1
        return -1

    def free(self, mID: int) -> int:
        ans = 0
        for i in range(self.n):
            if self.lst[i] == mID:
                ans += 1
                self.lst[i] = -1
        return ans


# 二分查找优化

from sortedcontainers import SortedList


class Allocator:
    def __init__(self, n: int):
        self.lst = SortedList([[0, n - 1]])  # 空闲区间 [a, b] 列表
        self.n = n
        self.dct = defaultdict(list)  # 已经分配 mid 对应区间 [a, b] 列表

    def allocate(self, size: int, mID: int) -> int:
        for a, b in self.lst:
            if b - a + 1 >= size:
                self.dct[mID].append([a, a + size - 1])
                self.lst.discard([a, b])
                if a + size <= b:
                    self.lst.add([a + size, b])
                return a
        return -1

    def free(self, mID: int) -> int:
        if not self.dct[mID]:
            return 0
        tmp = self.dct.pop(mID)
        ans = 0
        for a, b in tmp:
            ans += b - a + 1
            # 合并右区间
            while True:
                j = self.lst.bisect_left([a, a])
                if j < len(self.lst) and self.lst[j][0] == b + 1:
                    b = self.lst.pop(j)[1]
                else:
                    break
            # 合并左区间
            while True:
                j = self.lst.bisect_left([a, a]) - 1
                if j >= 0 and self.lst[j][1] == a - 1:
                    a = self.lst.pop(j)[0]
                else:
                    break
            self.lst.add([a, b])
        return ans
