class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for s in range(len(words)):
            i = len(words[s])
            for c in range(s+1,len(words)):
                if words[s]==words[c][:i] and words[s]==words[c][-i:]:
                    ans+=1
        return ans