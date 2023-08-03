# Created by shiyang07ca at 2023/08/03 13:33
# leetgo: dev
# https://leetcode.cn/problems/remove-comments/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # 匹配所有 // 和 /* */，后者用非贪婪模式。将所有匹配结果替换成空串。最后移除多余空行。
        return list(
            filter(
                None, re.sub("//.*|/\*(.|\n)*?\*/", "", "\n".join(source)).split("\n")
            )
        )

    # def removeComments2(self, source: List[str]) -> List[str]:
    #     ans = []
    #     flag = False
    #     t = []
    #     for s in source:
    #         if not flag and "//" in s and not ("/*" in s and "*/" in s):
    #             s = s.split("//")[0]
    #             if len(s) > 0:
    #                 ans.append(s)
    #         elif not flag and "/*" in s and "*/" in s:
    #             a = s.split("/*", 1)[0]
    #             b = s.rsplit("*/", 1)[1]
    #             if len(a + b):
    #                 ans.append(a + b)
    #         elif not flag and "/*" in s:
    #             s = s.split("/*", 1)[0]
    #             t = []
    #             t.append(s)
    #             flag = True
    #         elif flag and "*/" in s:
    #             s = s.split("*/", 1)[1]
    #             t.append(s)
    #             s = "".join(t)
    #             if len(s):
    #                 ans.append(s)
    #             flag = False
    #         elif flag:
    #             pass
    #         elif s:
    #             ans.append(s)
    #         # print(ans)
    #     return ans


# @lc code=end

if __name__ == "__main__":
    source: List[str] = deserialize("List[str]", read_line())
    ans = Solution().removeComments(source)

    print("\noutput:", serialize(ans))
