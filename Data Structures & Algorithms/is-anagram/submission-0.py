class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = sorted(tuple(s))
        second = sorted(tuple(t))
        return first == second