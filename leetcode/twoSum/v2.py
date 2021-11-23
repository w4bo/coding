from typing import List

def test_function(nums: List[int], target: int) -> List[int]:
    res = {}
    for i in range(len(nums)):
        c = nums[i]
        if c in res and c * 2 == target:
            return [i, res[c]]
        res[c] = i
        if target - c != c and target - c in res:
            return [i, res[target - c]]