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
def get_short_distance1(arr):
    if len(arr) == 0:
        return []


    if len(arr) == 1:
        return [[-1, -1]]

    ans = []
    for i, e in enumerate(arr):
        # 向右边查找
        if i == 0:
            for j, m in enumerate(arr[i + 1:]):
                if m < e:
                    ans.push([-1, j])
        # 向左边查找
        elif i == len(arr) - 1:
            for k, m in enumerate(arr[:i::-1]):
                if m < e:
                    ans.push([k, -1])
        # 向两边查找
        else:
            j, k = -1 , -1


    return ans


def get_short_distance2(arr):
    pass


import unittest


class TestMonotonicStack(unittest.TestCase):
    """
    """

    def test_monotonic_stack(self):
        self.assertEqual([
            [-1, 2],
            [0, 2],
            [-1, -1],
            [2, 5],
            [3, 5],
            [2, -1],
            [5, -1],
        ], get_short_distance1([3, 4, 1, 5, 6, 2, 7]))
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
