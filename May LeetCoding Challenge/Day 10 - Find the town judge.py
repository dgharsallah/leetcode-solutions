class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        indeg = [0] * (N + 1)
        outdeg = [0] * (N + 1)
        for p in trust:
            indeg[p[1]] = indeg[p[1]] + 1
            outdeg[p[0]] = outdeg[p[0]] + 1
        town_judge = -1
        num_judges = 0
        for i in range(1, N + 1):
            if indeg[i] == (N - 1) and outdeg[i] == 0:
                town_judge = i
                num_judges += 1
        if num_judges > 1:
            return False
        return town_judge
