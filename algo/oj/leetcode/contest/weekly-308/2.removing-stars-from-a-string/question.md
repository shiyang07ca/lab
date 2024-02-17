# [2390. 从字符串中移除星号][link] (Medium)

[link]: https://leetcode.cn/contest/weekly-contest-308/problems/removing-stars-from-a-string/


              <p>给你一个包含若干星号 <code>*</code> 的字符串 <code>s</code> 。</p>

<p>在一步操作中，你可以：</p>

<ul>
    <li>选中 <code>s</code> 中的一个星号。</li>
    <li>移除星号 <strong>左侧</strong> 最近的那个 <strong>非星号</strong> 字符，并移除该星号自身。</
li>
</ul>

<p>返回移除 <strong>所有</strong> 星号之后的字符串<strong>。</strong></p>

<p><strong>注意：</strong></p>

<ul>
    <li>生成的输入保证总是可以执行题面中描述的操作。</li>
    <li>可以证明结果字符串是唯一的。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &#34;leet**cod*e&#34;
<strong>输出：</strong>&#34;lecoe&#34;
<strong>解释：</strong>从左到右执行移除操作：
- 距离第 1 个星号最近的字符是 &#34;lee<em><strong>t</strong></em>**cod*e&#34; 中的 &#39;t&#39; ，s 
变为 &#34;lee*cod*e&#34; 。
- 距离第 2 个星号最近的字符是 &#34;le<em><strong>e</strong></em>*cod*e&#34; 中的 &#39;e&#39; ，s 变
为 &#34;lecod*e&#34; 。
- 距离第 3 个星号最近的字符是 &#34;leco<em><strong>d</strong></em>*e&#34; 中的 &#39;d&#39; ，s 变为 
&#34;lecoe&#34; 。
不存在其他星号，返回 &#34;lecoe&#34; 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &#34;erase*****&#34;
<strong>输出：</strong>&#34;&#34;
<strong>解释：</strong>整个字符串都会被移除，所以返回空字符串。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
    <li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
    <li><code>s</code> 由小写英文字母和星号 <code>*</code> 组成</li>
    <li><code>s</code> 可以执行上述操作</li>
</ul>

            
