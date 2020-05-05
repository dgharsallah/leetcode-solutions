class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if wordList is None or len(wordList) == 0:
            return 0
        wordList.append(beginWord)
        source, destination = -1, -1
        l = len(wordList[0])
        g = [[] for _ in range(len(wordList))]
        idx = {}
        for i in range(len(wordList)):
            idx[wordList[i]] = i
        for i in range(len(wordList)):
            if wordList[i] == beginWord:
                source = i
            if wordList[i] == endWord:
                destination = i
            for j in range(len(wordList[i])):
                for c in ascii_lowercase:
                    ns = wordList[i][:j] + c + wordList[i][j + 1:]
                    v = idx.get(ns, -1)
                    if v != -1:
                        g[i].append(v)
                        g[v].append(i)
        if source == -1 or destination == -1:
            return 0
        q = [(1, source)]
        vis = [False] * len(wordList)
        vis[source] = True
        while len(q) > 0:
            cost, u = heapq.heappop(q)
            if u == destination:
                return cost
            for v in g[u]:
                if not vis[v]:
                    heapq.heappush(q, (cost + 1, v))
                    vis[v] = True
        return 0
