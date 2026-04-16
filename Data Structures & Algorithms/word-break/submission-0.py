class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(cur, memo):
            if len(cur) == 0:
                return True
            if cur in memo:
                return memo[cur]

            for word in wordDict:
                if cur.startswith(word):
                    if dfs(cur[len(word):], memo):
                        memo[cur] = True
                        return True

            memo[cur] = False
            return False

        return dfs(s, {})