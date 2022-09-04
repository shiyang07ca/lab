"""

# TODO

6170. 会议室 III


给你一个整数 n ，共有编号从 0 到 n - 1 的 n 个会议室。

给你一个二维整数数组 meetings ，其中 meetings[i] = [starti, endi] 表示一场会议将会在 半闭 时间区间 [starti, endi) 举办。所有 starti 的值 互不相同 。

会议将会按以下方式分配给会议室：

每场会议都会在未占用且编号 最小 的会议室举办。
如果没有可用的会议室，会议将会延期，直到存在空闲的会议室。延期会议的持续时间和原会议持续时间 相同 。
当会议室处于未占用状态时，将会优先提供给原 开始 时间更早的会议。
返回举办最多次会议的房间 编号 。如果存在多个房间满足此条件，则返回编号 最小 的房间。

半闭区间 [a, b) 是 a 和 b 之间的区间，包括 a 但 不包括 b 。



示例 1：

输入：n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
输出：0
解释：
- 在时间 0 ，两个会议室都未占用，第一场会议在会议室 0 举办。
- 在时间 1 ，只有会议室 1 未占用，第二场会议在会议室 1 举办。
- 在时间 2 ，两个会议室都被占用，第三场会议延期举办。
- 在时间 3 ，两个会议室都被占用，第四场会议延期举办。
- 在时间 5 ，会议室 1 的会议结束。第三场会议在会议室 1 举办，时间周期为 [5,10) 。
- 在时间 10 ，两个会议室的会议都结束。第四场会议在会议室 0 举办，时间周期为 [10,11) 。
会议室 0 和会议室 1 都举办了 2 场会议，所以返回 0 。



示例 2：

输入：n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
输出：1
解释：
- 在时间 1 ，所有三个会议室都未占用，第一场会议在会议室 0 举办。
- 在时间 2 ，会议室 1 和 2 未占用，第二场会议在会议室 1 举办。
- 在时间 3 ，只有会议室 2 未占用，第三场会议在会议室 2 举办。
- 在时间 4 ，所有三个会议室都被占用，第四场会议延期举办。
- 在时间 5 ，会议室 2 的会议结束。第四场会议在会议室 2 举办，时间周期为 [5,10) 。
- 在时间 6 ，所有三个会议室都被占用，第五场会议延期举办。
- 在时间 10 ，会议室 1 和 2 的会议结束。第五场会议在会议室 1 举办，时间周期为 [10,12) 。
会议室 1 和会议室 2 都举办了 2 场会议，所以返回 1 。


提示：

1 <= n <= 100
1 <= meetings.length <= 105
meetings[i].length == 2
0 <= starti < endi <= 5 * 105
starti 的所有值 互不相同


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/meeting-rooms-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


"""
用两个小顶堆模拟：

idle 维护在 start i 时刻空闲的会议室的编号；
using 维护在 start i 时刻使用中的会议室的结束时间和编号。

对 meetings 按照开始时间排序，然后遍历 meetings，按照题目要求模拟即可，具体模拟方式见代码。

复杂度分析
时间复杂度：O(n+m(\log n + \log m))O(n+m(logn+logm))，其中 mm 为 \textit{meetings}meetings 的长度。注意每个会议至多入堆出堆各一次。
空间复杂度：O(n)O(n)。
相似题目
1606. 找到处理最多请求的服务器
1882. 使用服务器处理任务



作者：endlesscheng
链接：https://leetcode.cn/problems/meeting-rooms-iii/solution/shuang-dui-mo-ni-pythonjavacgo-by-endles-ctwc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        cnt = [0] * n
        idle = list(range(n))  # 空闲会议室编号
        using = []  # (结束时间，会议室编号)
        meetings.sort(key=lambda m: m[0])
        for st, end in meetings:
            # 在 st 时刻前正在开会的会议室中，已经结束的会议室弹出来，加入到空闲会议室中
            while using and using[0][0] <= st:
                heappush(idle, heappop(using)[1])  # 维护在 st 时刻空闲的会议室
            if len(idle) == 0:
                e, i = heappop(using)  # 没有可用的会议室，那么弹出一个最早结束的会议室
                end += e - st  # 更新当前会议的结束时间
            else:
                i = heappop(idle)
            cnt[i] += 1
            heappush(using, (end, i))  # 使用一个会议室
        ans = 0
        for i, c in enumerate(cnt):
            if c > cnt[ans]:
                ans = i
        return ans
