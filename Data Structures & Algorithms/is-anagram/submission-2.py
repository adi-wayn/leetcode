class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashset = defaultdict(int)

        for c in s:
            hashset[c] += 1
        
        for c in t:
            if c in hashset:
                hashset[c] -= 1
        
        for c in hashset:
            if hashset[c] != 0:
                return False
        
        return True