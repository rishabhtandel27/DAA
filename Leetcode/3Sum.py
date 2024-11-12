class Solution:
    def threeSum(self, nums):
        # Sort the array to apply the two-pointer approach
        nums.sort()
        triplets = []
        
        for i in range(len(nums)):
            # Skip duplicates for the first element to avoid repeating the same triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move pointers inward
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return triplets
