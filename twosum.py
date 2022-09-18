class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target - nums[i] == nums[j]:
                    result.append(i)
                    result.append(j)
        return result

# a = Solution()
# a.twoSum([3,2,4],6)