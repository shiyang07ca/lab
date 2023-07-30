# [6957. 统计范围内的步进数字数目][link] (Hard)

[link]: https://leetcode.cn/contest/weekly-contest-356/problems/count-stepping-numbers-in-range/


              <p>给你两个正整数 <code>low</code> 和 <code>high</code> ，都用字符串表示，请你统计闭区
间 <code>[low, high]</code> 内的 <strong>步进数字</strong> 数目。</p>

<p>如果一个整数相邻数位之间差的绝对值都 <strong>恰好</strong> 是 <code>1</code> ，那么这个数字被称为
<strong>步进数字</strong> 。</p>

<p>请你返回一个整数，表示闭区间 <code>[low, high]</code> 之间步进数字的数目。</p>

<p>由于答案可能很大，请你将它对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 后返回。</p>

<p><b>注意：</b>步进数字不能有前导 0 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>low = &#34;1&#34;, high = &#34;11&#34;
<b>输出：</b>10
<strong>解释：</strong>区间 [1,11] 内的步进数字为 1 ，2 ，3 ，4 ，5 ，6 ，7 ，8 ，9 和 10 。总共有 1
0 个步进数字。所以输出为 10 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>low = &#34;90&#34;, high = &#34;101&#34;
<b>输出：</b>2
<strong>解释：</strong>区间 [90,101] 内的步进数字为 98 和 101 。总共有 2 个步进数字。所以输出为 2 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
    <li><code>1 &lt;= int(low) &lt;= int(high) &lt; 10<sup>100</sup></code></li>
    <li><code>1 &lt;= low.length, high.length &lt;= 100</code></li>
    <li><code>low</code> 和 <code>high</code> 只包含数字。</li>
    <li><code>low</code> 和 <code>high</code> 都不含前导 0 。</li>
</ul>

            
