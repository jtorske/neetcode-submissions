class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_list = list(t)

        for i in range(len(s)):
                if s[i] not in t_list:
                    return False
                t_list.remove(s[i])
        return True