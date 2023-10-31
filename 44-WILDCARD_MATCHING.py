# 44. WILDCARD MATCHING - HARD
# https://leetcode.com/problems/wildcard-matching/

class Solution(object):
    def isMatch(self, s, p):
        s_pointer = 0
        p_pointer = 0
        match = 0
        star_idx = -1

        while s_pointer < len(s):
            # If the characters match or the pattern character is a '?'
            if p_pointer < len(p) and (p[p_pointer] == '?' or p[p_pointer] == s[s_pointer]):
                s_pointer += 1
                p_pointer += 1
            # If the pattern character is '*'
            elif p_pointer < len(p) and p[p_pointer] == '*':
                star_idx = p_pointer
                match = s_pointer
                p_pointer += 1
            # If a mismatch occurs and there was a previous '*' in the pattern
            elif star_idx != -1:
                p_pointer = star_idx + 1
                match += 1
                s_pointer = match
            # If there's a mismatch and no '*' in the pattern to backtrack
            else:
                return False

        # Check for remaining characters in the pattern
        while p_pointer < len(p) and p[p_pointer] == '*':
            p_pointer += 1

        return p_pointer == len(p)

# Example usage:
solution = Solution()

# Example 1
s1 = "aa"
p1 = "a"
print(solution.isMatch(s1, p1))  # Output: False

# Example 2
s2 = "aa"
p2 = "*"
print(solution.isMatch(s2, p2))  # Output: True

# Example 3
s3 = "cb"
p3 = "?a"
print(solution.isMatch(s3, p3))  # Output: False
