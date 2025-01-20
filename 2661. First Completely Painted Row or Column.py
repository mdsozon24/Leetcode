class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hmap = {mat[i][j]:(i,j) for i in range(len(mat)) for j in range(len(mat[0]))}
        row = [0]*len(mat)
        col = [0]*len(mat[0])
        for k in range(len(arr)):
            i,j = hmap[arr[k]]
            row[i]+=1
            col[j]+=1
            if row[i]==len(mat[0]) or col[j]==len(mat):
                return k
        