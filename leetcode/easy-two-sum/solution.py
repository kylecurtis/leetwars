from typing import List


# SOLUTION
def twoSum(nums: List[int], target: int) -> List[int]:
    # Create a dictionary to keep track of number indices we've seen
    seen = {}

    # Iterate through each number and its index in the list
    for i, n in enumerate(nums):
        # Calculate the value we need to find to get the target sum
        diff = target - n

        # If we've seen the required value before, return its index along with the current index
        if diff in seen:
            return [seen[diff], i]

        # Store the current number and its index in the dictionary
        seen[n] = i


# TEST FUNCTION
def test_twoSum():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
