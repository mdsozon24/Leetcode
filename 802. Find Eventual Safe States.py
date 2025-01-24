class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        ans = []
        safe = {}
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for n in graph[i]:
                if not dfs(n):
                    return safe[n]
            safe[i] = True
            return True
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans