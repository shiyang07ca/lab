r"""


生成窗口最大值数组

有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置。

例如，数组为[4，3，5，4，3，3，6，7]，窗口大小为3时


[4, 3, 5], 4, 3, 3, 6, 7   5

4, [3, 5, 4], 3, 3, 6, 7   5

4, 3, [5, 4, 3], 3, 6, 7   5

4, 3, 5, [4, 3, 3], 6, 7   4

4, 3, 5, 4, [3, 3, 6], 7   6

4, 3, 5, 4, 3, [3, 6, 7]   7

输入：整型数组arr，窗口大小为w。

输出：一个长度为n-w+1的数组res，res[i]表示每一种窗口状态下的最大值。以本题为例，结果应该返回{5，5，5，4，6，7}。



"""


def get_max_window(arr, w):
    if not arr or w < 1:
        return None

    ans = [-1] * (len(arr) - w + 1)
    qmax = []
    index = 0
    for i, e in enumerate(arr):
        while qmax and arr[qmax[-1]] <= e:
            qmax.pop()

        qmax.append(i)

        # 如果qmax队头的下标等于i-w，说明当前qmax队头的下标已过期,
        # 弹出当前队头的下标即可
        if qmax[0] == i - w:
            qmax.pop(0)

        # 窗口已经出现，开始计算最大值
        if i >= w - 1:
            ans[index] = arr[qmax[0]]
            index += 1

    return ans



import unittest

class Test(unittest.TestCase):
    def test(self):
        print('aaa')
        self.assertEqual(
            [5, 5, 5, 4, 6, 7],
            get_max_window([4, 3, 5, 4, 3, 3, 6, 7], 3)
        )


if __name__ == '__main__':
    unittest.main()
