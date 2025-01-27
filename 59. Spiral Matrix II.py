class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        val = 1
        mat = [[0]*n for _ in range(n)]
        top,down,left,right = 0,n,0,n
        while val <= n**2 :
            for i in range(left,right):
                mat[top][i] = val
                val+=1
            top+=1
            for i in range(top,down):
                mat[i][right-1] = val
                val+=1
            right-=1
            for i in range(right-1,left-1,-1):
                mat[down-1][i] = val
                val+=1
            down-=1
            for i in range(down-1,top-1,-1):
                mat[i][left] = val
                val+=1
            left+=1
        return mat