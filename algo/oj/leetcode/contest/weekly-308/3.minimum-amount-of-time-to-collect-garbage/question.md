# [2391. 收集垃圾的最少总时间][link] (Medium)

[link]: https://leetcode.cn/contest/weekly-contest-308/problems/minimum-amount-of-time-to-collect-garbage/


              <p>给你一个下标从 <strong>0</strong> 开始的字符串数组 <code>garbage</code> ，其中 <cod
e>garbage[i]</code> 表示第 <code>i</code> 个房子的垃圾集合。<code>garbage[i]</code> 只包含字符 <code
>&#39;M&#39;</code> ，<code>&#39;P&#39;</code> 和 <code>&#39;G&#39;</code> ，但可能包含多个相同字符
，每个字符分别表示一单位的金属、纸和玻璃。垃圾车收拾 <strong>一</strong> 单位的任何一种垃圾都需要花
费 <code>1</code> 分钟。</p>

<p>同时给你一个下标从 <strong>0</strong> 开始的整数数组 <code>travel</code> ，其中 <code>travel[i]</
code> 是垃圾车从房子 <code>i</code> 行驶到房子 <code>i + 1</code> 需要的分钟数。</p>

<p>城市里总共有三辆垃圾车，分别收拾三种垃圾。每辆垃圾车都从房子 <code>0</code> 出发，<strong>按顺序<
/strong> 到达每一栋房子。但它们 <strong>不是必须</strong> 到达所有的房子。</p>

<p>任何时刻只有 <strong>一辆</strong> 垃圾车处在使用状态。当一辆垃圾车在行驶或者收拾垃圾的时候，另外
两辆车 <strong>不能</strong> 做任何事情。</p>

<p>请你返回收拾完所有垃圾需要花费的 <strong>最少</strong> 总分钟数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>garbage = [&#34;G&#34;,&#34;P&#34;,&#34;GP&#34;,&#34;GG&#34;], travel = [2,4,3]
<b>输出：</b>21
<strong>解释：</strong>
收拾纸的垃圾车：
1. 从房子 0 行驶到房子 1
2. 收拾房子 1 的纸垃圾
3. 从房子 1 行驶到房子 2
4. 收拾房子 2 的纸垃圾
收拾纸的垃圾车总共花费 8 分钟收拾完所有的纸垃圾。
收拾玻璃的垃圾车：
1. 收拾房子 0 的玻璃垃圾
2. 从房子 0 行驶到房子 1
3. 从房子 1 行驶到房子 2
4. 收拾房子 2 的玻璃垃圾
5. 从房子 2 行驶到房子 3
6. 收拾房子 3 的玻璃垃圾
收拾玻璃的垃圾车总共花费 13 分钟收拾完所有的玻璃垃圾。
由于没有金属垃圾，收拾金属的垃圾车不需要花费任何时间。
所以总共花费 8 + 13 = 21 分钟收拾完所有垃圾。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>garbage = [&#34;MMM&#34;,&#34;PGM&#34;,&#34;GP&#34;], travel = [3,10]
<b>输出：</b>37
<strong>解释：</strong>
收拾金属的垃圾车花费 7 分钟收拾完所有的金属垃圾。
收拾纸的垃圾车花费 15 分钟收拾完所有的纸垃圾。
收拾玻璃的垃圾车花费 15 分钟收拾完所有的玻璃垃圾。
总共花费 7 + 15 + 15 = 37 分钟收拾完所有的垃圾。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
    <li><code>2 &lt;= garbage.length &lt;= 10<sup>5</sup></code></li>
    <li><code>garbage[i]</code> 只包含字母 <code>&#39;M&#39;</code> ，<code>&#39;P&#39;</code> 和 <c
ode>&#39;G&#39;</code> 。</li>
    <li><code>1 &lt;= garbage[i].length &lt;= 10</code></li>
    <li><code>travel.length == garbage.length - 1</code></li>
    <li><code>1 &lt;= travel[i] &lt;= 100</code></li>
</ul>

            
