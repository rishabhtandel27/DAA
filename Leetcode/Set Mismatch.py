class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        seen = set()
        duplicate = -1
        missing = -1
        
        # Find the duplicate number
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)
        
        # Find the missing number
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break
                
        return [duplicate, missing]

# Example usage
sol = Solution()

# Test case
nums1 = [1, 2, 2, 4]
output1 = sol.findErrorNums(nums1)
print(output1)  # Output: [2, 3]
