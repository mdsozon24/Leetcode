class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        pre,left,right = 0,0,0
        for i,c in enumerate(boxes):
            if c=='1':
                pre+=i
                left+=1
        for char in boxes:
            ans.append(pre)
            if char=='1':
                left-=1
                right+=1
            pre-=(left-right)
        return ans