class Solution:
    def missingNumber(self, nums):
        n = len(nums)  # Length of the array
        sum_expected = n * (n + 1) // 2  # Expected sum of numbers from 0 to n
        sum_actual = sum(nums)  # Actual sum of numbers in the array
        
        # The missing number is the difference
        return sum_expected - sum_actual

# Example usage
sol = Solution()

# Test case
nums1 = [3, 0, 1]
output1 = sol.missingNumber(nums1)
print(output1)  # Output: 2

# Additional test case
nums2 = [0, 1]
output2 = sol.missingNumber(nums2)
print(output2)  # Output: 2

# Additional test case
nums3 = [0]
output3 = sol.missingNumber(nums3)
print(output3)  # Output: 1
