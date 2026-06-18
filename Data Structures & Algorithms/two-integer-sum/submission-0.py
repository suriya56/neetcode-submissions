class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                first_index = num_map[complement]
                second_index = index
                return sorted([first_index, second_index])
            num_map[num] = index
