class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        new_str = list(s1)
        
        
        if s1[2] == s2[0]:
            new_str[0] = s1[2]
            new_str[2] = s1[0]

        if new_str == list(s2):
            return True

        if s1[3] == s2[1]:
            new_str[1] = s1[3]
            new_str[3] = s1[1]

        if new_str == list(s2):
            return True

        return False


print(Solution().canBeEqual(s1="abcd", s2="cdab"))

print(Solution().canBeEqual(s1="abcd", s2="dacb"))
