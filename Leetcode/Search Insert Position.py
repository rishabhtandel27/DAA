class Solution:
    def searchInsert(self, nums, target):  # Use 'searchInsert' as the method name
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid  # Target found, return the index
            elif nums[mid] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
        
        return left  # Return the index where the target should be inserted

# Example usage:
solution = Solution()
nums = [1, 3, 5, 6]
target = 5
output = solution.searchInsert(nums, target)
print(output)  # Output: 2

# Example usage for inserting a new target
target = 2
output = solution.searchInsert(nums, target)
print(output)  # Output: 1
