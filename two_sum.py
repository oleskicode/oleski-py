def two_sum(nums: list[int], t: int )-> list[int]:

    """ Two Sum. Given an array of integers nums and an integer target,
    return indexes of two numbers that add up to target.
    Each input has exactly 1 solution.
    Examples:
    nums = [2,7,11,15], target = 9 → [0,1]
    nums = [3,2,4], target = 6 → [1,2] """

    for first in range(len(nums)):
        for second in range( first+1, len(nums)):
            if nums[first] + nums[second] == t:
                return [first, second]
            # print(j, end=" ")
    return "No solution"


print(two_sum([0,1,2,3,4],3))
print(two_sum([2,7,11,15], 9))
print(two_sum([2,7,11,15], 26))
print(two_sum([3,2,4,5], 7))
print(two_sum([3,1,4,6,0], 6))
