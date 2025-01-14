class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        val = 0
        ans = []
        for i in range(len(A)):
            if A[i] in seen:
                val+=1
            seen.add(A[i])
            if B[i] in seen:
                val+=1
            seen.add(B[i])
            ans.append(val)

        return ans