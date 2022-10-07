/*

  作者：yxc
  链接：https://www.acwing.com/blog/content/277/
  来源：AcWing
  著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

**/


bool check(int x) {/* ... */} // 检查x是否满足某种性质


// 区间[l, r]被划分成[l, mid]和[mid + 1, r]时使用：
int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = (l + r) >> 1;
        if (check(mid)) r = mid;    // check()判断mid是否满足性质
        else l = mid + 1;
    }
    return l;
}


// 区间[l, r]被划分成[l, mid - 1]和[mid, r]时使用：
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = (l + r + 1) >> 1;
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}
