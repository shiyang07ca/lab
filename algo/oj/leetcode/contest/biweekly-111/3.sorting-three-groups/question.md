# [6941. 将三个组排序][link] (Medium)

[link]: https://leetcode.cn/contest/biweekly-contest-111/problems/sorting-three-groups/


              <p>给你一个下标从 <strong>0</strong> 开始长度为 <code>n</code> 的整数数组 <code>nums</
code> 。<br/>
<br/>
从 <code>0</code> 到 <code>n - 1</code> 的数字被分为编号从 <code>1</code> 到 <code>3</code> 的三个组
，数字 <code>i</code> 属于组 <code>nums[i]</code> 。注意，有的组可能是 <strong>空的</strong> 。<br/>
<br/>
你可以执行以下操作任意次：</p>

<ul>
    <li>选择数字 <code>x</code> 并改变它的组。更正式的，你可以将 <code>nums[x]</code> 改为数字 <code
>1</code> 到 <code>3</code> 中的任意一个。</li>
</ul>

<p>你将按照以下过程构建一个新的数组 <code>res</code> ：</p>

<ol>
    <li>将每个组中的数字分别排序。</li>
    <li>将组 <code>1</code> ，<code>2</code> 和 <code>3</code> 中的元素 <strong>依次</strong> 连接以
得到 <code>res</code> 。</li>
</ol>

<p>如果得到的 <code>res</code> 是 <strong>非递减</strong>顺序的，那么我们称数组 <code>nums</code> 是
<strong>美丽数组</strong> 。</p>

<p>请你返回将<em> </em><code>nums</code> 变为 <strong>美丽数组</strong> 需要的最少步数。</p>

<p> </p>

<p><strong class="example">示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,1,3,2,1]
<b>输出：</b>3
<b>解释：</b>以下三步操作是最优方案：
1. 将 nums[0] 变为 1 。
2. 将 nums[2] 变为 1 。
3. 将 nums[3] 变为 1 。
执行以上操作后，将每组中的数字排序，组 1 为 [0,1,2,3,4] ，组 2 和组 3 都为空。所以 res 等于 [0,1,2,3
,4] ，它是非递减顺序的。
三步操作是最少需要的步数。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,3,2,1,3,3]
<b>输出：</b>2
<b>解释：</b>以下两步操作是最优方案：
1. 将 nums[1] 变为 1 。
2. 将 nums[2] 变为 1 。
执行以上操作后，将每组中的数字排序，组 1 为 [0,1,2,3] ，组 2 为空，组 3 为 [4,5] 。所以 res 等于 [0,
1,2,3,4,5] ，它是非递减顺序的。
两步操作是最少需要的步数。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre><b>输入：</b>nums = [2,2,2,2,3,3]
<b>输出：</b>0
<b>解释：</b>不需要执行任何操作。
组 1 为空，组 2 为 [0,1,2,3] ，组 3 为 [4,5] 。所以 res 等于 [0,1,2,3,4,5] ，它是非递减顺序的。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
    <li><code>1 &lt;= nums.length &lt;= 100</code></li>
    <li><code>1 &lt;= nums[i] &lt;= 3</code></li>
</ul>

            
