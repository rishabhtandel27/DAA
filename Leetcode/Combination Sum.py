class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, target, current_combination):
            # Base case: if target is 0, add the current combination to the result
            if target == 0:
                result.append(list(current_combination))
                return
            
            # Explore the candidates starting from the current index to allow repetition
            for i in range(start, len(candidates)):
                if candidates[i] > target:  # No need to continue if the number exceeds the target
                    continue
                current_combination.append(candidates[i])  # Include the current candidate
                backtrack(i, target - candidates[i], current_combination)  # Recurse with reduced target
                current_combination.pop()  # Backtrack: remove the last element to try the next one
        
        # Start the backtracking with the initial index 0, target, and empty combination
        backtrack(0, target, [])
        
        return result
