"""
Given an array of strings, group anagrams together.

Example:

    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]

Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""
from collections import defaultdict


def solution(arr):
    temp = defaultdict(list)
    for i in arr:
        temp["".join(sorted(i))].append(i)

    return temp.values()


a = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution(a))
