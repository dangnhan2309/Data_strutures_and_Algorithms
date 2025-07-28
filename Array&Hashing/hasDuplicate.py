 
from typing import List
class Solution:
    def hasDuplicate(self,nums: List[int])-> bool: 
        bag = []
        for num in nums: 
            if num in bag: 
                return True 
            bag.append(num)
        return False
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 1]
    solution = Solution()
    print(solution.hasDuplicate(nums))  # Output: True