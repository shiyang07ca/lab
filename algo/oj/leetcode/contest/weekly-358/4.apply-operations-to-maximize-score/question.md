# [7023. 操作使得分最大][link] (Hard)

[link]: https://leetcode.cn/contest/weekly-contest-358/problems/apply-operations-to-maximize-score/


              <p>给你一个长度为 <code>n</code> 的正整数数组 <code>nums</code> 和一个整数 <code>k</co
de> 。</p>

<p>一开始，你的分数为 <code>1</code> 。你可以进行以下操作至多 <code>k</code> 次，目标是使你的分数最
大：</p>

<ul>
    <li>选择一个之前没有选过的 <strong>非空</strong> 子数组 <code>nums[l, ..., r]</code> 。</li>
    <li>从 <code>nums[l, ..., r]</code> 里面选择一个 <strong>质数分数</strong> 最高的元素 <code>x</c
ode> 。如果多个元素质数分数相同且最高，选择下标最小的一个。</li>
    <li>将你的分数乘以 <code>x</code> 。</li>
</ul>

<p><code>nums[l, ..., r]</code> 表示 <code>nums</code> 中起始下标为 <code>l</code> ，结束下标为 <cod
e>r</code> 的子数组，两个端点都包含。</p>

<p>一个整数的 <strong>质数分数</strong> 等于 <code>x</code> 不同质因子的数目。比方说， <code>300</co
de> 的质数分数为 <code>3</code> ，因为 <code>300 = 2 * 2 * 3 * 5 * 5</code> 。</p>

<p>请你返回进行至多 <code>k</code> 次操作后，可以得到的 <strong>最大分数</strong> 。</p>

<p>由于答案可能很大，请你将结果对 <code>10<sup>9 </sup>+ 7</code> 取余后返回。</p>

<p> </p>

<p><strong class="example">示例 1：</strong></p>

<pre><b>输入：</b>nums = [8,3,9,3,8], k = 2
<b>输出：</b>81
<b>解释：</b>进行以下操作可以得到分数 81 ：
- 选择子数组 nums[2, ..., 2] 。nums[2] 是子数组中唯一的元素。所以我们将分数乘以 nums[2] ，分数变为 1
* 9 = 9 。
- 选择子数组 nums[2, ..., 3] 。nums[2] 和 nums[3] 质数分数都为 1 ，但是 nums[2] 下标更小。所以我们将
分数乘以 nums[2] ，分数变为 9 * 9 = 81 。
81 是可以得到的最高得分。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre><b>输入：</b>nums = [19,12,14,6,10,18], k = 3
<b>输出：</b>4788
<b>解释：</b>进行以下操作可以得到分数 4788 ：
- 选择子数组 nums[0, ..., 0] 。nums[0] 是子数组中唯一的元素。所以我们将分数乘以 nums[0] ，分数变为 1
* 19 = 19 。
- 选择子数组 nums[5, ..., 5] 。nums[5] 是子数组中唯一的元素。所以我们将分数乘以 nums[5] ，分数变为 1
9 * 18 = 342 。
- 选择子数组 nums[2, ..., 3] 。nums[2] 和 nums[3] 质数分数都为 2，但是 nums[2] 下标更小。所以我们将
分数乘以 nums[2] ，分数变为  342 * 14 = 4788 。
4788 是可以得到的最高的分。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
    <li><code>1 &lt;= nums.length == n &lt;= 10<sup>5</sup></code></li>
    <li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
    <li><code>1 &lt;= k &lt;= min(n * (n + 1) / 2, 10<sup>9</sup>)</code></li>
</ul>

            
