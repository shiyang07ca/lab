class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n < 1:
            return ''

        # ['a', 'b', ... 'z']
        char_arr = [chr(n) for n in range(ord('a'), ord('z') + 1)]
        ans = []
        for i in range(n):
            # 剩余位置全为 'z' 的和
            max_rest = (n - i - 1) * 26
            # 剩余目标小于所有位置都放 z 的情况
            if k <= max_rest:
                ans.append('a')
            else:
                ans.append(char_arr[k - max_rest - 1])
            k -= ord(ans[-1]) - ord('a') + 1

        return ''.join(ans)
