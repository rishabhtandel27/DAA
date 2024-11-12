class Solution:
    def containsDuplicate(self, nums):
        seen = set()  # Initialize an empty set to track seen numbers
        
        for num in nums:
            if num in seen:  # Check if the number is already in the set
                return True  # Duplicate found
            seen.add(num)  # Add the number to the set
        
        return False  # No duplicates found

# Example usage
sol = Solution()

# Test case 1
nums1 = [1, 2, 3, 1]
output1 = sol.containsDuplicate(nums1)
print(output1)  # Output: true

# Test case 2
nums2 = [1, 2, 3, 4]
output2 = sol.containsDuplicate(nums2)
print(output2)  # Output: false

# Test case 3
nums3 = [5, 6, 7, 8, 5]
output3 = sol.containsDuplicate(nums3)
print(output3)  # Output: true
