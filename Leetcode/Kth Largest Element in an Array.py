import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # Create a min-heap with the first k elements from nums
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # Transform list into a heap in O(k) time

        # Iterate through the rest of the numbers in nums
        for num in nums[k:]:
            if num > min_heap[0]:  # If the current number is larger than the smallest in the heap
                heapq.heappop(min_heap)  # Remove the smallest element
                heapq.heappush(min_heap, num)  # Add the current number

        # The root of the min-heap is the kth largest element
        return min_heap[0]

# Example usage:
solution = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
output = solution.findKthLargest(nums, k)
print(output)  # Output: 5


        
