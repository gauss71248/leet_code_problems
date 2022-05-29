import math
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def find_closest_element(l: List[int], x: int):
            if len(l) == 1:
                return l[0]
            else:
                if l[math.floor(len(l)/2)]<x:
                    return find_closest_element(l[math.floor(len(l)/2):],x)
                else:
                    return find_closest_element(l[:math.floor(len(l)/2)],x)
        if target in nums:
            return nums.index(target)
        else:
            closest_element = find_closest_element(nums,target)
            closest_element_index = nums.index(closest_element)
            if closest_element < target:
                return closest_element_index + 1
            else:
                return closest_element_index