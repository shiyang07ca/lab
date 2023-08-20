# Created by shiyang07ca at 2023/08/19 23:35
# leetgo: dev
# https://leetcode.cn/problems/number-of-beautiful-integers-in-the-range/
# https://leetcode.cn/contest/biweekly-contest-111/problems/number-of-beautiful-integers-in-the-range/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: 数位dp


class Solution:
    # 链接：https://leetcode.cn/problems/number-of-beautiful-integers-in-the-range/solutions/2396206/shu-wei-dppythonjavacgo-by-endlesscheng-4gvw/
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def calc(high: int) -> int:
            s = str(high)

            @cache  # 记忆化搜索
            def dfs(i: int, val: int, diff: int, is_limit: bool, is_num: bool) -> int:
                if i == len(s):
                    return int(is_num and val == 0 and diff == 0)  # 找到了一个合法数字
                res = 0
                if not is_num:  # 可以跳过当前数位
                    res = dfs(i + 1, val, diff, False, False)
                d0 = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
                up = (
                    int(s[i]) if is_limit else 9
                )  # 如果前面填的数字都和 high 的一样，那么这一位至多填 s[i]（否则就超过 high 啦）
                for d in range(d0, up + 1):  # 枚举要填入的数字 d
                    res += dfs(
                        i + 1,
                        (val * 10 + d) % k,
                        diff + d % 2 * 2 - 1,
                        is_limit and d == up,
                        True,
                    )
                return res

            return dfs(0, 0, 0, True, False)

        return calc(high) - calc(low - 1)


# @lc code=end

if __name__ == "__main__":
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfBeautifulIntegers(low, high, k)

    print("\noutput:", serialize(ans))
