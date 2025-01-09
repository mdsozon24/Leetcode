class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        dic_s = Counter(s)
        dic_t = Counter(t)
        for k, v in dic_s.items():
            if k in dic_t:
                ans += abs(v - dic_t[k])
            else:
                ans += v
        for k, v in dic_t.items():
            if k not in dic_s:
                ans += v
        return ans