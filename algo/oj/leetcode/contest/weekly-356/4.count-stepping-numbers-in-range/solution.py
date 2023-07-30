# Created by shiyang07ca at 2023/07/30 10:34
# leetgo: dev
# https://leetcode.cn/problems/count-stepping-numbers-in-range/
# https://leetcode.cn/contest/weekly-contest-356/problems/count-stepping-numbers-in-range/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: 数位dp

"""
# 链接：
https://leetcode.cn/problems/count-stepping-numbers-in-range/solutions/2364624/shu-wei-dp-tong-yong-mo-ban-by-endlessch-h8fj/

定义 calc(n) 表示不超过 n 的步进数字数目。那么答案就是
       calc(high) - calc(low-1)
     = calc(high) - calc(low) + valid(low)


定义 f(i, pre, isLimit, isNum) 表示构造第 i 位及其之后数位的合法方案数，其余参数
的含义为：

* pre 表示上一个数位的值。如果 isNum 为 false，可以忽略 pre

* isLimit 表示当前是否受到了 n 的约束（注意要构造的数组不能超过 n）。若为真，则
第 i 位填入的数字至多为 n[i]，否则可以是 9。如果在受到约束的情况下填了 s[i]，那
么后续填入的数字仍会受到 n 的约束。例如 n=123，那么 i=0 填的是 1 的话，i=1 的这
一位至多填 2.

* isNum 表示 i 前面的数位是否填了数字。若为假，则当前位可以跳过（不填数字），
或者要填入的数字至少为 1；若为真，则要填入的数字可以从 0 开始。例如 n=123，在
i=0 时跳过的话，相当于后面要构造的是一个 99 以内的数字了；如果 i=1 不跳过，那么
相当于构造一个 10 到 99 的两位数，如果 i=1 也跳过，相当于构造的是一个 9 以内的数
字。

"""


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7

        def calc(s: str) -> int:
            @cache  # 记忆化搜索
            def f(i: int, pre: int, is_limit: bool, is_num: bool) -> int:
                if i == len(s):
                    return int(is_num)  # is_num 为 True 表示得到了一个合法数字
                res = 0
                if not is_num:  # 可以跳过当前数位
                    res = f(i + 1, pre, False, False)
                low = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
                up = (
                    int(s[i]) if is_limit else 9
                )  # 如果前面填的数字都和 s 的一样，那么这一位至多填 s[i]（否则就超过 s 啦）
                for d in range(low, up + 1):  # 枚举要填入的数字 d
                    if not is_num or abs(d - pre) == 1:  # 第一位数字随便填，其余必须相差 1
                        res += f(i + 1, d, is_limit and d == up, True)
                return res % MOD

            return f(0, 0, True, False)

        return (calc(high) - calc(str(int(low) - 1))) % MOD


# @lc code=end

if __name__ == "__main__":
    low: str = deserialize("str", read_line())
    high: str = deserialize("str", read_line())
    ans = Solution().countSteppingNumbers(low, high)

    print("\noutput:", serialize(ans))
