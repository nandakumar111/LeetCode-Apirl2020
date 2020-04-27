"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

    1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
    3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    5. An empty string is also valid.

Example 1:
    Input: "()"
    Output: True

Example 2:
    Input: "(*)"
    Output: True

Example 3:
    Input: "(*))"
    Output: True

Note:
    The string size will be in the range [1, 100].
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # balance = 0
        # for i in s:
        #     if i == '(' or i == '*':
        #         balance += 1
        #     else:
        #         balance -= 1
        #         if balance == -1:
        #             return False
        # balance = 0
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == ')' or s[i] == '*':
        #         balance += 1
        #     else:
        #         balance -= 1
        #         if balance == -1:
        #             return False
        #
        # return True
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0


s = Solution()
print(s.checkValidString("()"))
