class Solution:
    def selfDividingNumbers(self, left, right):
        def is_self_dividing(num):
            original_num = num
            while num > 0:
                digit = num % 10
                if digit == 0 or original_num % digit != 0:
                    return False
                num //= 10
            return True

        return [num for num in range(left, right + 1) if is_self_dividing(num)]

# Example usage
sol = Solution()

left = 1
right = 22
print(sol.selfDividingNumbers(left, right))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

        
