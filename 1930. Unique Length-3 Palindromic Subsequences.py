class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mp = defaultdict(list)
        ans = 0
        for i in range(len(s)):
            mp[s[i]].append(i)
        for m in mp:
            if len(mp[m])>=2:
                ans+=len(set(s[mp[m][0]+1:mp[m][-1]]))
        return ans