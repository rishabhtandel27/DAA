class Solution:
    def findTheDifference(self, s, t):
        result = 0
        
        # XOR all characters in s
        for char in s:
            result ^= ord(char)
        
        # XOR all characters in t
        for char in t:
            result ^= ord(char)
        
        # The result will be the ASCII value of the added character
        return chr(result)

# Example usage
sol = Solution()

# Test case
s = "abcd"
t = "abcde"
output = sol.findTheDifference(s, t)
print(output)  # Output: "e"
