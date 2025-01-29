class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lm,m = 0,len(matrix)-1
        ln,n = 0,len(matrix[0])-1
        while lm <= m:
            midm = (lm+m)//2
            if matrix[midm][0] <= target and matrix[midm][-1] >= target:
                while ln<=n:
                    mid = (ln+n)//2
                    if matrix[midm][mid]==target:
                        return True
                    elif matrix[midm][mid] < target:
                        ln = mid+1
                    else:
                        n = mid-1
                return False
            elif matrix[midm][0] > target:
                m = midm-1
            else:
                lm = midm+1
        return False