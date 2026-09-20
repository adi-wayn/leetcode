from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        longest_word_length = max(len(word) for word in wordDict) if wordDict else 0

        for i in range(1, len(s) + 1):
            for j in range(max(0, i - longest_word_length), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]