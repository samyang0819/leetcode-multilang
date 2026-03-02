class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        last_non_zero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1
        
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0

# Example usage:
solution = Solution()
nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print(nums)  # Output: [1,3,12,0,0]

nums = [0,0,1]
solution.moveZeroes(nums)
print(nums)  # Output: [1,0,0]

nums = [0,0,0]
solution.moveZeroes(nums)
print(nums)  # Output: [0,0,0]
