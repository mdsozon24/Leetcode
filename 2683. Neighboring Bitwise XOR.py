class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for n in derived:
            ans^=n
        return True if ans==0 else False