class Solution:
    def arrayPairSum(self, nums):
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Calculate the sum of the minimums
        max_sum = sum(nums[i] for i in range(0, len(nums), 2))
        
        return max_sum

# Example usage
sol = Solution()

# Test case
nums1 = [1, 4, 3, 2]
output1 = sol.arrayPairSum(nums1)
print(output1)  # Output: 4
