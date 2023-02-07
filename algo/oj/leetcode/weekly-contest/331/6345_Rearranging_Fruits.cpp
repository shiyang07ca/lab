// 作者：tsreaper
// 链接：https://leetcode.cn/problems/rearranging-fruits/solution/si-wei-by-tsreaper-5oi7/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution {
public:
    long long minCost(vector<int>& A, vector<int>& B) {
        int n = A.size();

        // mp：水果在所有篮子里出现的次数
        // mpA：水果在第一个篮子里出现的次数
        // mpB：水果在第二个篮子里出现的次数
        unordered_map<int, int> mp, mpA, mpB;
        for (int x : A) mp[x]++, mpA[x]++;
        for (int y : B) mp[y]++, mpB[y]++;
        // 检查是否有出现奇数次的水果
        for (auto it = mp.begin(); it != mp.end(); it++) if ((it->second) % 2 == 1) return -1;

        // 计算两个篮子中多出来哪些水果，把它们都放在同一个 vector 里并排序
        vector<int> vec;
        for (auto it = mpA.begin(); it != mpA.end(); it++) {
            int have = it->second, goal = mp[it->first] / 2;
            if (have > goal) for (int i = 0; i < have - goal; i++) vec.push_back(it->first);
        }
        for (auto it = mpB.begin(); it != mpB.end(); it++) {
            int have = it->second, goal = mp[it->first] / 2;
            if (have > goal) for (int i = 0; i < have - goal; i++) vec.push_back(it->first);
        }
        sort(vec.begin(), vec.end());

        // 求所有水果里的最小值
        int mn = 1e9;
        for (int x : A) mn = min(mn, x);
        for (int x : B) mn = min(mn, x);

        // 套公式计算答案
        long long ans = 0;
        for (int i = 0; i < vec.size() / 2; i++) ans += min(vec[i], mn * 2);
        return ans;
    }
};
