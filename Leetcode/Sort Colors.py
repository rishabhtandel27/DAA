class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Example usage
sol = Solution()

# Test case
nums1 = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

# Additional test cases
nums2 = [1, 2, 0]
sol.sortColors(nums2)
print(nums2)  # Output: [0, 1, 2]

nums3 = [0, 1, 2]
sol.sortColors(nums3)
print(nums3)  # Output: [0, 1, 2]

nums4 = [2, 2, 1, 1, 0, 0]
sol.sortColors(nums4)
print(nums4)  # Output: [0, 0, 1, 1, 2, 2]
