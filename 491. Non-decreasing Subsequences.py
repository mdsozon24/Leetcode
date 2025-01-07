class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        def solve(s,arr):
            if len(arr)>1:
                ans.add(tuple(arr))
            for i in range(s,n):
                if not arr or arr[-1]<=nums[i]:
                    solve(i+1,arr+[nums[i]])
                else:
                    solve(i+1,arr)
        solve(0,[])
        return list(map(list,ans))