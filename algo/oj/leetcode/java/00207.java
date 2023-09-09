// Created by shiyang07ca at 2023/09/09 12:55
// leetgo: dev
// https://leetcode.cn/problems/course-schedule/

// @lc code=begin

class Solution {
    public boolean canFinish(int n, int[][] edges) {
        List<Integer>[] g = new List[n];
        Arrays.setAll(g, i -> new ArrayList<>());
        int[] indeg = new int[n];
        for (var e : edges) {
            int y = e[0], x = e[1];
            g[x].add(y);
            indeg[y] += 1;
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) q.offer(i);
        }
        int cnt = 0;
        while (!q.isEmpty()) {
            int x = q.poll();
            cnt++;
            for (int y : g[x]) {
                if (--indeg[y] == 0) {
                    q.offer(y);
                }
            }
        }
        return cnt == n;
    }
}
// @lc code=end
