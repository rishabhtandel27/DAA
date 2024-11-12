from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        # Count the frequency of each character
        freq = Counter(s)
        length = 0
        odd_found = False
        
        # Iterate over the frequency counts
        for count in freq.values():
            if count % 2 == 0:
                # If the count is even, add all of them to the palindrome length
                length += count
            else:
                # If the count is odd, add the maximum even part (count - 1)
                length += count - 1
                odd_found = True
        
        # If there was any odd count, we can add one character in the middle
        if odd_found:
            length += 1
        
        return length
