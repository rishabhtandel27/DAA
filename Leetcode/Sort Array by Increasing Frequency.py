from collections import Counter

class Solution:
    def frequencySort(self, nums):
        # Count the frequency of each number
        freq = Counter(nums)
        
        # Sort by frequency (ascending), and by value (descending) if frequencies are equal
        return sorted(nums, key=lambda x: (freq[x], -x))

# Example usage
sol = Solution()

# Example input
nums = [1, 1, 2, 2, 2, 3]
print(sol.frequencySort(nums))  # Output: [3, 1, 1, 2, 2, 2]
