# Created by shiyang07ca at 2023/05/07 13:38
# https://leetcode.cn/problems/frequency-tracker/
# https://leetcode.cn/contest/weekly-contest-344/problems/frequency-tracker/

"""
6417. 频率跟踪器 (Medium)
请你设计并实现一个能够对其中的值进行跟踪的数据结构，并支持对
频率相关查询进行应答。

实现 `FrequencyTracker` 类：

- `FrequencyTracker()`：使用一个空数组初始化 `FrequencyTrack
er` 对象。
- `void add(int number)`：添加一个 `number` 到数据结构中。
- `void deleteOne(int number)`：从数据结构中删除一个 `number
` 。数据结构 **可能不包含** `number` ，在这种情况下不删除任
何内容。
- `bool hasFrequency(int frequency)`: 如果数据结构中存在出现
`frequency` 次的数字，则返回 `true`，否则返回 `false`。

**示例 1：**

```
输入
["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]
输出
[null, null, null, true]

解释
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(3); // 数据结构现在包含 [3]
frequencyTracker.add(3); // 数据结构现在包含 [3, 3]
frequencyTracker.hasFrequency(2); // 返回 true ，因为 3 出现
2 次

```

**示例 2：**

```
输入
["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
[[], [1], [1], [1]]
输出
[null, null, null, false]

解释
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(1); // 数据结构现在包含 [1]
frequencyTracker.deleteOne(1); // 数据结构现在为空 []
frequencyTracker.hasFrequency(1); // 返回 false ，因为数据结
构为空

```

**示例 3：**

```
输入
["FrequencyTracker", "hasFrequency", "add", "hasFrequency"]
[[], [2], [3], [1]]
输出
[null, false, null, true]

解释
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.hasFrequency(2); // 返回 false ，因为数据结
构为空
frequencyTracker.add(3); // 数据结构现在包含 [3]
frequencyTracker.hasFrequency(1); // 返回 true ，因为 3 出现
1 次

```

**提示：**

- `1 <= number <= 10⁵`
- `1 <= frequency <= 10⁵`
- 最多调用 `add`、 `deleteOne` 和 `hasFrequency` **共计** `2
* 10⁵` 次

"""
from collections import *

from typing import *
from leetgo_py import *

# @lc code=begin


class FrequencyTracker:
    def __init__(self):
        self.cnt = Counter()
        self.fq = Counter()

    def add(self, n: int) -> None:
        self.fq[self.cnt[n]] -= 1
        self.cnt[n] += 1
        self.fq[self.cnt[n]] += 1

    def deleteOne(self, n: int) -> None:
        if self.cnt[n] == 0:
            return
        self.fq[self.cnt[n]] -= 1
        self.cnt[n] -= 1
        self.fq[self.cnt[n]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.fq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = FrequencyTracker()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                number: int = deserialize("int", method_params[0])
                obj.add(number)
                output.append("null")
            case "deleteOne":
                method_params = split_array(params[i])
                number: int = deserialize("int", method_params[0])
                obj.deleteOne(number)
                output.append("null")
            case "hasFrequency":
                method_params = split_array(params[i])
                frequency: int = deserialize("int", method_params[0])
                ans = serialize(obj.hasFrequency(frequency))
                output.append(ans)

    print("output: " + join_array(output))
