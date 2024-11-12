class Solution:
    def sortArray(self, nums):
        # Merge Sort function
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2  # Find the middle of the array
                left_half = arr[:mid]  # Left half
                right_half = arr[mid:]  # Right half

                # Recursively split and sort both halves
                merge_sort(left_half)
                merge_sort(right_half)

                # Merge the sorted halves
                i = j = k = 0

                # Copy data to temporary arrays left_half[] and right_half[]
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                # Checking if any element was left
                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort(nums)  # Call the merge_sort function to sort the array
        return nums

# Example usage:
solution = Solution()
nums = [5, 2, 3, 1]
output = solution.sortArray(nums)
print(output)  # Output: [1, 2, 3, 5]
