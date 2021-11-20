from typing import List

def test_function(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i > j and nums[j] + nums[i] == target:
                return [i, j]