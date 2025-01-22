class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        mat = [[-1]*n for _ in range(m)]
        que = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    que.append((i,j))
                    mat[i][j] = 0
        while que:
            i,j = que.popleft()
            if i+1 < m and mat[i+1][j]==-1:
                que.append((i+1,j))
                mat[i+1][j] = mat[i][j]+1
            if i-1 >= 0 and mat[i-1][j]==-1:
                que.append((i-1,j))
                mat[i-1][j] = mat[i][j]+1
            if j+1 < n and mat[i][j+1]==-1:
                que.append((i,j+1))
                mat[i][j+1] = mat[i][j]+1
            if j-1 >= 0 and mat[i][j-1]==-1:
                que.append((i,j-1))
                mat[i][j-1] = mat[i][j]+1
        return mat