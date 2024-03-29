"""

# TODO
# tag: trie


6183. 字符串的前缀分数和
给你一个长度为 n 的数组 words ，该数组由 非空 字符串组成。

定义字符串 word 的 分数 等于以 word 作为 前缀 的 words[i] 的数目。

例如，如果 words = ["a", "ab", "abc", "cab"] ，那么 "ab" 的分数是 2 ，因为 "ab" 是 "ab" 和 "abc" 的一个前缀。
返回一个长度为 n 的数组 answer ，其中 answer[i] 是 words[i] 的每个非空前缀的分数 总和 。

注意：字符串视作它自身的一个前缀。



示例 1：

输入：words = ["abc","ab","bc","b"]
输出：[5,4,3,2]
解释：对应每个字符串的答案如下：
- "abc" 有 3 个前缀："a"、"ab" 和 "abc" 。
- 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" ，1 个字符串的前缀为 "abc" 。
总计 answer[0] = 2 + 2 + 1 = 5 。
- "ab" 有 2 个前缀："a" 和 "ab" 。
- 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" 。
总计 answer[1] = 2 + 2 = 4 。
- "bc" 有 2 个前缀："b" 和 "bc" 。
- 2 个字符串的前缀为 "b" ，1 个字符串的前缀为 "bc" 。
总计 answer[2] = 2 + 1 = 3 。
- "b" 有 1 个前缀："b"。
- 2 个字符串的前缀为 "b" 。
总计 answer[3] = 2 。



示例 2：

输入：words = ["abcd"]
输出：[4]
解释：
"abcd" 有 4 个前缀 "a"、"ab"、"abc" 和 "abcd"。
每个前缀的分数都是 1 ，总计 answer[0] = 1 + 1 + 1 + 1 = 4 。


提示：

1 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] 由小写英文字母组成


"""


"""

根据题意，我们可以用字典树存储所有字符串，由于每个节点都是其子树节点的前缀，题干中的分数就是经过该节点的字符串个数，即以该节点为前缀的字符串的个数。

然后 DFS 这颗字典树，累加路径上的分数，就可以得到每个字符串的所有非空前缀的分数总和了。

代码实现时，由于可能有相同字符串，每个字符串对应的节点需要用一个列表存储该字符串在 words 中的所有下标。


复杂度分析
- 时间复杂度：O(L)，其中 L 为 word i 的长度之和。
- 空间复杂度：O(L)


作者：endlesscheng
链接：https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/solution/by-endlesscheng-ghfr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Node:
    __slots__ = "son", "ids", "score"

    def __init__(self):
        self.son = defaultdict(Node)
        self.ids = []
        self.score = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Node()
        for i, word in enumerate(words):
            cur = root
            for c in word:
                cur = cur.son[c]
                cur.score += 1  # 更新所有前缀的分数
            cur.ids.append(i)

        ans = [0] * len(words)

        def dfs(node: Node, sum: int) -> None:
            sum += node.score  # 累加分数，即可得到答案
            for i in node.ids:
                ans[i] = sum
            for child in node.son.values():
                if child:
                    dfs(child, sum)

        dfs(root, 0)
        return ans
