
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i
        return []


class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        for i in range(len(string_x)):
            if string_x[i] == string_x[len(string_x) - i - 1]:
                count = count + 1
        if count == len(string_x):
            return True
        else:
            return False
        