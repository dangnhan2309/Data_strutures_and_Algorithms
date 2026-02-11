from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 2> len(nums) or len(nums) > 1000 : 
            return False
        if -10000000 > target or target > 10000000 :
            return False
        stack = {}
        for num in nums : 
            if num > 10000000 or num<=-10000000:
                return False
            stack[num] = stack.get(num,0) +1 
        for i,num in enumerate(nums) : 
            chose = target - num 
            if chose == num : 
                stack[num] -=1
            if chose in stack and stack[chose] > 0:
               return [i,nums.index(chose,i+1)]
        return False 
if __name__ == "__main__":  
    nums = [2,11,7 , 15]
    target = 9

    solution = Solution()
    print(solution.twoSum(nums, target))  # Output: [0, 1]
    