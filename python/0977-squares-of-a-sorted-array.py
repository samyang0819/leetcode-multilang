class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result

# Example usage:
solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))  # Output: [0,1,9,16,100]
print(solution.sortedSquares([-7,-3,2,3,11]))  # Output: [4,9,9,49,121]
print(solution.sortedSquares([-5,-3,-2,-1]))  # Output: [1,4,9,25]
print(solution.sortedSquares([0,1,2,3,4]))  # Output: [0,1,4,9,16]
print(solution.sortedSquares([-2,0,2]))  # Output: [0,4,4]
print(solution.sortedSquares([-3,-2,-1]))  # Output: [1,4,9]
print(solution.sortedSquares([-1]))  # Output: [1]
print(solution.sortedSquares([1]))  # Output: [1]
print(solution.sortedSquares([-1,0,1]))  # Output: [0,1,1]
print(solution.sortedSquares([-2,-1,0]))  # Output: [0,1,4]
print(solution.sortedSquares([-2,-1,0,1,2]))  # Output: [0,1,4,4,4]
