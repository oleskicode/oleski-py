def three_consecutive_odds(nums: list[int]) -> bool:
    """Three Consecutive Odds"""
    if len(nums) < 3:  # input validation
        return False

    counter = 0
    for num in nums:
        if num % 2 == 1:
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0
    return False


print(three_consecutive_odds(([2, 6, 4, 1])))
# Output: false
# Explanation: There are no three consecutive odds.

print(three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
