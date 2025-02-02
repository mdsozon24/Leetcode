class Solution:
    def check(self, nums: List[int]) -> bool:
        a=0
        for i in range(len(nums)):
            list_1=list()
            list_1=nums[i:]+nums[0:i]
            b=sorted(list_1)
            if list_1 == b:
               return True
        return False