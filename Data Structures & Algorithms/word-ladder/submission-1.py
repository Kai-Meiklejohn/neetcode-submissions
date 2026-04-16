class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        adj = defaultdict(list)

        def one_diff(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        # build graph
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if one_diff(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])

        q = deque([beginWord])
        visited = set([beginWord])
        steps = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return steps

                for nei in adj[word]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            steps += 1

        return 0
        