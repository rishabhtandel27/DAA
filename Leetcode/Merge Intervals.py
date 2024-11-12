class Solution:
    def merge(self, intervals):
        # Step 1: Sort the intervals by the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If merged list is empty or there's no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)  # No overlap, add the interval
            else:
                # Overlap detected, merge with the last interval in merged
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

# Example usage
sol = Solution()

# Test case
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
output1 = sol.merge(intervals1)
print(output1)  # Output: [[1, 6], [8, 10], [15, 18]]

# Additional test cases
intervals2 = [[1, 4], [2, 3]]
output2 = sol.merge(intervals2)
print(output2)  # Output: [[1, 4]]

intervals3 = [[1, 5], [6, 8], [2, 4]]
output3 = sol.merge(intervals3)
print(output3)  # Output: [[1, 5], [6, 8]]

intervals4 = [[1, 2], [3, 4], [5, 6]]
output4 = sol.merge(intervals4)
print(output4)  # Output: [[1, 2], [3, 4], [5, 6]]
