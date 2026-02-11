class Solution:
    def isAnagram(self,s: str , t:str)->bool :
        return True if set(s) == set(t) and len(s) == len(t) else False
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        count={}
        for char in s: 
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True if all(value == 0 for value in count.values()) else False
if __name__ == "__main__": 
    s = "bbcc"
    t = "ccbc"
    solution = Solution()
    print(solution.isAnagram(s, t))  # Output: True
    print(solution.isAnagram2(s, t))  # Output: True

    count={"a": 1, "b": 2, "c": 2}
    print(count.get("d",0))
      # Output: {'a': 1, 'b': 2, 'c': 2}


