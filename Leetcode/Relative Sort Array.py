class Solution:
    def relativeSortArray(self, arr1, arr2):
       
        order_map = {val: idx for idx, val in enumerate(arr2)}
     
        return sorted(arr1, key=lambda x: (order_map.get(x, len(arr2)), x))

