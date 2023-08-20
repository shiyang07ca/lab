# [8014. 循环增长使字符串子序列等于另一个字符串][link] (Medium)

[link]: https://leetcode.cn/contest/biweekly-contest-111/problems/make-string-a-subsequence-using-cyclic-increments/


              <p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>str1</code> 和 <code>str2</cod
e> 。</p>

<p>一次操作中，你选择 <code>str1</code> 中的若干下标。对于选中的每一个下标 <code>i</code> ，你将 <co
de>str1[i]</code> <strong>循环</strong> 递增，变成下一个字符。也就是说 <code>&#39;a&#39;</code> 变成
<code>&#39;b&#39;</code> ，<code>&#39;b&#39;</code> 变成 <code>&#39;c&#39;</code> ，以此类推，<code>
&#39;z&#39;</code> 变成 <code>&#39;a&#39;</code> 。</p>

<p>如果执行以上操作 <strong>至多一次</strong> ，可以让 <code>str2</code> 成为 <code>str1</code> 的子
序列，请你返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p><b>注意：</b>一个字符串的子序列指的是从原字符串中删除一些（可以一个字符也不删）字符后，剩下字符按
照原本先后顺序组成的新字符串。</p>

<p> </p>

<p><strong class="example">示例 1：</strong></p>

<pre><b>输入：</b>str1 = &#34;abc&#34;, str2 = &#34;ad&#34;
<b>输出：</b>true
<b>解释：</b>选择 str1 中的下标 2 。
将 str1[2] 循环递增，得到 &#39;d&#39; 。
因此，str1 变成 &#34;abd&#34; 且 str2 现在是一个子序列。所以返回 true 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre><b>输入：</b>str1 = &#34;zc&#34;, str2 = &#34;ad&#34;
<b>输出：</b>true
<b>解释：</b>选择 str1 中的下标 0 和 1 。
将 str1[0] 循环递增得到 &#39;a&#39; 。
将 str1[1] 循环递增得到 &#39;d&#39; 。
因此，str1 变成 &#34;ad&#34; 且 str2 现在是一个子序列。所以返回 true 。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre><b>输入：</b>str1 = &#34;ab&#34;, str2 = &#34;d&#34;
<b>输出：</b>false
<b>解释：</b>这个例子中，没法在执行一次操作的前提下，将 str2 变为 str1 的子序列。
所以返回 false 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
    <li><code>1 &lt;= str1.length &lt;= 10<sup>5</sup></code></li>
    <li><code>1 &lt;= str2.length &lt;= 10<sup>5</sup></code></li>
    <li><code>str1</code> 和 <code>str2</code> 只包含小写英文字母。</li>
</ul>

            
