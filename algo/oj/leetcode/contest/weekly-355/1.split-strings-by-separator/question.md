# [6921. 按分隔符拆分字符串][link] (Easy)

[link]: https://leetcode.cn/contest/weekly-contest-355/problems/split-strings-by-separator/


              <p>给你一个字符串数组 <code>words</code> 和一个字符 <code>separator</code> ，请你按 <c
ode>separator</code> 拆分 <code>words</code> 中的每个字符串。</p>

<p>返回一个由拆分后的新字符串组成的字符串数组，<strong>不包括空字符串</strong> 。</p>

<p><strong>注意</strong></p>

<ul>
    <li><code>separator</code> 用于决定拆分发生的位置，但它不包含在结果字符串中。</li>
    <li>拆分可能形成两个以上的字符串。</li>
    <li>结果字符串必须保持初始相同的先后顺序。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>words = [&#34;one.two.three&#34;,&#34;four.five&#34;,&#34;six&#34;], sep
arator = &#34;.&#34;
<strong>输出：</strong>[&#34;one&#34;,&#34;two&#34;,&#34;three&#34;,&#34;four&#34;,&#34;five&#34;,&#
34;six&#34;]
<strong>解释：</strong>在本示例中，我们进行下述拆分：

&#34;one.two.three&#34; 拆分为 &#34;one&#34;, &#34;two&#34;, &#34;three&#34;
&#34;four.five&#34; 拆分为 &#34;four&#34;, &#34;five&#34;
&#34;six&#34; 拆分为 &#34;six&#34; 

因此，结果数组为 [&#34;one&#34;,&#34;two&#34;,&#34;three&#34;,&#34;four&#34;,&#34;five&#34;,&#34;six
&#34;] 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>words = [&#34;$easy$&#34;,&#34;$problem$&#34;], separator = &#34;$&#34;
<strong>输出：</strong>[&#34;easy&#34;,&#34;problem&#34;]
<strong>解释：</strong>在本示例中，我们进行下述拆分：

&#34;$easy$&#34; 拆分为 &#34;easy&#34;（不包括空字符串）
&#34;$problem$&#34; 拆分为 &#34;problem&#34;（不包括空字符串）

因此，结果数组为 [&#34;easy&#34;,&#34;problem&#34;] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>words = [&#34;|||&#34;], separator = &#34;|&#34;
<strong>输出：</strong>[]
<strong>解释：</strong>在本示例中，&#34;|||&#34; 的拆分结果将只包含一些空字符串，所以我们返回一个空
数组 [] 。 </pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
    <li><code>1 &lt;= words.length &lt;= 100</code></li>
    <li><code>1 &lt;= words[i].length &lt;= 20</code></li>
    <li><code>words[i]</code> 中的字符要么是小写英文字母，要么就是字符串 <code>&#34;.,|$#@&#34;</cod
e> 中的字符（不包括引号）</li>
    <li><code>separator</code> 是字符串 <code>&#34;.,|$#@&#34;</code> 中的某个字符（不包括引号）</li
>
</ul>

            
