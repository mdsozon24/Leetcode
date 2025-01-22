class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans_mat = [[-1]*n for _ in range(m)]
        que = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    que.append((i,j))
                    ans_mat[i][j] = 0
        while que:
            i,j = que.popleft()
            if i+1 < m and ans_mat[i+1][j]==-1:
                que.append((i+1,j))
                ans_mat[i+1][j] = ans_mat[i][j]+1
            if i-1 >= 0 and ans_mat[i-1][j]==-1:
                que.append((i-1,j))
                ans_mat[i-1][j] = ans_mat[i][j]+1
            if j+1 < n and ans_mat[i][j+1]==-1:
                que.append((i,j+1))
                ans_mat[i][j+1] = ans_mat[i][j]+1
            if j-1 >= 0 and ans_mat[i][j-1]==-1:
                que.append((i,j-1))
                ans_mat[i][j-1] = ans_mat[i][j]+1
        return ans_mat