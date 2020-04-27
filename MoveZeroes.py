"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""


def move_zero(arr, n):
    count = 0

    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1


a = [0, 1, 0, 3, 12]
move_zero(a, len(a))
print(a)
