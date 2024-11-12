class Solution:
    def sortPeople(self, names, heights):
    
        return [name for name, height in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)]

sol = Solution()

names1 = ["Mary", "John", "Emma"]
heights1 = [180, 165, 170]
print(sol.sortPeople(names1, heights1))  # Output: ["Mary", "Emma", "John"]


names2 = ["Alice", "Bob", "Bob"]
heights2 = [155, 185, 150]
print(sol.sortPeople(names2, heights2))  # Output: ["Bob", "Alice", "Bob"]


names2 = ["Alice", "Bob", "Bob"]
heights2 = [155, 185, 150]
print(sol.sortPeople(names2, heights2)) 
