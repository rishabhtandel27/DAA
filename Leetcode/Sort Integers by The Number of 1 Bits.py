class Solution:
    def sortByBits(self, arr):
        # Sort the array with a key that considers the number of 1's and the integer itself
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Example usage
sol = Solution()

# Test case
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
output = sol.sortByBits(arr)
print(output)  # Output: [0, 1, 2, 4, 8, 3, 5, 6, 7]
