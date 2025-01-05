class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        arr = []
        vaw = {'a','e','i','o','u'}
        for chr in words:
            if chr[0] in vaw and chr[-1] in vaw:
                arr.append(1)
            else:
                arr.append(0)
        for i in range(1,len(arr)):
            arr[i] = arr[i]+arr[i-1]
        for s,e in queries:
            if s==0 :
                ans.append(arr[e])
            else:
                ans.append(arr[e]-arr[s-1])
        return ans