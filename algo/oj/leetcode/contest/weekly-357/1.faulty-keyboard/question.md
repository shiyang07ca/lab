# [6925. 故障键盘][link] (Easy)

[link]: https://leetcode.cn/contest/weekly-contest-357/problems/faulty-keyboard/


              <p>你的笔记本键盘存在故障，每当你在上面输入字符 <code>&#39;i&#39;</code> 时，它会反转
你所写的字符串。而输入其他字符则可以正常工作。</p>

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>s</code> ，请你用故障键盘依次输入每个字符。<
/p>

<p>返回最终笔记本屏幕上输出的字符串。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &#34;string&#34;
<strong>输出：</strong>&#34;rtsng&#34;
<strong>解释：</strong>
输入第 1 个字符后，屏幕上的文本是：&#34;s&#34; 。
输入第 2 个字符后，屏幕上的文本是：&#34;st&#34; 。
输入第 3 个字符后，屏幕上的文本是：&#34;str&#34; 。
因为第 4 个字符是 &#39;i&#39; ，屏幕上的文本被反转，变成 &#34;rts&#34; 。
输入第 5 个字符后，屏幕上的文本是：&#34;rtsn&#34; 。
输入第 6 个字符后，屏幕上的文本是： &#34;rtsng&#34; 。
因此，返回 &#34;rtsng&#34; 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &#34;poiinter&#34;
<strong>输出：</strong>&#34;ponter&#34;
<strong>解释：</strong>
输入第 1 个字符后，屏幕上的文本是：&#34;p&#34; 。
输入第 2 个字符后，屏幕上的文本是：&#34;po&#34; 。
因为第 3 个字符是 &#39;i&#39; ，屏幕上的文本被反转，变成 &#34;op&#34; 。
因为第 4 个字符是 &#39;i&#39; ，屏幕上的文本被反转，变成 &#34;po&#34; 。
输入第 5 个字符后，屏幕上的文本是：&#34;pon&#34; 。
输入第 6 个字符后，屏幕上的文本是：&#34;pont&#34; 。
输入第 7 个字符后，屏幕上的文本是：&#34;ponte&#34; 。
输入第 8 个字符后，屏幕上的文本是：&#34;ponter&#34; 。
因此，返回 &#34;ponter&#34; 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
    <li><code>1 &lt;= s.length &lt;= 100</code></li>
    <li><code>s</code> 由小写英文字母组成</li>
    <li><code>s[0] != &#39;i&#39;</code></li>
</ul>

            
