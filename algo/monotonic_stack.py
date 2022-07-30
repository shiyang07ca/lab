r"""



* 描述
  给定一个不含有重复值的数组arr，找到每一个i位置左边和右边离i位置最近
  且值比arr[i]小的位置。返回所有位置相应的信息。

* 举例

arr = [3, 4, 1, 5, 6, 2, 7]

返回二维数组
[
  [-1, 2],
  [0, 2],
  [-1, -1],
  [2, 5],
  [3, 5],
  [2, -1],
  [5, -1]
]



"""


# brute force
def get_near_less_no_repeat1(arr):
    if len(arr) == 0:
        return []

    ans = []
    for i, e in enumerate(arr):
        left, right = -1, -1

        cur = i - 1
        while cur >=0:
            if arr[cur] < e:
                left = cur
                break
            cur -= 1

        cur = i + 1
        while cur < len(arr):
            if arr[cur] < e:
                right = cur
                break
            cur += 1

        ans.append([left, right])

    return ans


def get_near_less_no_repeat2(arr):
    ans = [[]] * len(arr)
    stack = []

    for i, e in enumerate(arr):
        # 如果破坏了栈单调性
        while(stack and arr[stack[-1]] > e):
            pop_index = stack.pop()
            left = stack[-1] if stack else -1
            ans[pop_index] = [left, i]

        stack.append(i)

    while stack:
        pop_index = stack.pop()
        left = stack[-1] if stack else -1
        ans[pop_index] = [left, -1]

    return ans


# 存在重复元素的单调栈
def get_near_less(arr):
    ans = [[]] * len(arr)
    stack = []

    for i, e in enumerate(arr):
        # 如果破坏了栈单调性
        while(stack and arr[stack[-1][0]] > e):
            pop_indexs = stack.pop()
            # 取位于下面位置列表中，最晚加入的那个
            left = stack[-1][-1] if stack else -1
            for p_i in pop_indexs:
                ans[p_i] = [left, i]

        if stack and arr[stack[-1][0]] == e:
            stack[-1].append(i)
        else:
            stack.append([i])

    while stack:
        pop_indexs = stack.pop()
        # 取位于下面位置列表中，最晚加入的那个
        left = stack[-1][-1] if stack else -1
        for p_i in pop_indexs:
            ans[p_i] = [left, -1]

    return ans


import unittest


class TestMonotonicStack(unittest.TestCase):
    """
    """

    def test_monotonic_stack1(self):
        self.assertEqual([
            [-1, -1],
        ], get_near_less_no_repeat1([3]))
        self.assertEqual([
            [-1, 2],
            [0, 2],
            [-1, -1],
            [2, 5],
            [3, 5],
            [2, -1],
            [5, -1],
        ], get_near_less_no_repeat1([3, 4, 1, 5, 6, 2, 7]))

    def test_monotonic_stack2(self):
        self.assertEqual([
            [-1, -1],
        ], get_near_less_no_repeat2([3]))
        self.assertEqual([
            [-1, 2],
            [0, 2],
            [-1, -1],
            [2, 5],
            [3, 5],
            [2, -1],
            [5, -1],
        ], get_near_less_no_repeat2([3, 4, 1, 5, 6, 2, 7]))


    def test_monotonic_stack3(self):
        self.assertEqual([
            [-1, -1],
        ], get_near_less_no_repeat2([3]))
        self.assertEqual([
            [-1, 2],
            [0, 2],
            [-1, -1],
            [2, 5],
            [3, 5],
            [2, -1],
            [5, -1],
        ], get_near_less([3, 4, 1, 5, 6, 2, 7]))
        self.assertEqual([
            [-1, 1],   # 0
            [-1, -1],  # 1
            [1, 7],    # 2
            [2, 4],    # 3
            [1, 7],    # 4
            [4, 6],    # 5
            [1, 7],    # 6
            [1, -1],   # 7
            [1, -1],   # 8
        ], get_near_less([3, 1, 3, 4, 3 ,5 ,3 ,2, 2]))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
