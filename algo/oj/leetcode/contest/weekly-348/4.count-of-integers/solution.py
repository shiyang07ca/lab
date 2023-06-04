# Created by shiyang07ca at 2023/06/04 13:07
# https://leetcode.cn/problems/count-of-integers/
# https://leetcode.cn/contest/weekly-contest-348/problems/count-of-integers/

"""
6396. 统计整数数目 (Hard)
给你两个数字字符串 `num1` 和 `num2` ，以及两个整数 `max_sum` 和 `min_sum` 。如果一个整数 `x` 满足以
下条件，我们称它是一个好整数：

- `num1 <= x <= num2`
- `min_sum <= digit_sum(x) <= max_sum`.

请你返回好整数的数目。答案可能很大，请返回答案对 `10⁹ + 7` 取余后的结果。

注意， `digit_sum(x)` 表示 `x` 各位数字之和。

**示例 1：**

```
输入：num1 = "1", num2 = "12", min_num = 1, max_num = 8
输出：11
解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11
。

```

**示例 2：**

```
输入：num1 = "1", num2 = "5", min_num = 1, max_num = 5
输出：5
解释：数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5 。

```

**提示：**

- `1 <= num1 <= num2 <= 10²²`
- `1 <= min_sum <= max_sum <= 400`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def f(s: string) -> int:
            @cache
            def f(i: int, sum: int, is_limit: bool) -> int:
                # 从高到低位枚举 i，sum 表示当前数位和，is_limit 表示当前位置的
                # 上界是否收到 s[i] 的限制
                if sum > max_sum:  # 非法
                    return 0
                if i == len(s):
                    return int(sum >= min_sum)
                res = 0
                up = int(s[i]) if is_limit else 9
                for d in range(up + 1):  # 枚举要填入的数字 d
                    res += f(i + 1, sum + d, is_limit and d == up)
                return res % MOD

            return f(0, 0, True)

        ans = f(num2) - f(num1) + (min_sum <= sum(map(int, num1)) <= max_sum)
        return ans % MOD


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-of-integers/solutions/2296043/shu-wei-dp-tong-yong-mo-ban-pythonjavacg-9tuc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# @lc code=end

if __name__ == "__main__":
    num1: str = deserialize("str", read_line())
    num2: str = deserialize("str", read_line())
    min_sum: int = deserialize("int", read_line())
    max_sum: int = deserialize("int", read_line())
    ans = Solution().count(num1, num2, min_sum, max_sum)

    print("\noutput:", serialize(ans))
