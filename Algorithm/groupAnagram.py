class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for values,index in emerate(strs).items:
        	print(f"{values}")


 if __name__=="__main__":
 	case1 = ["act","pots","tops","cat","stop","hat"]
 	case2 = ["x"]
 	case3 = [""]

 	sol = Solution()
 	print(sol.groupAnagrams(case1))
 	print(sol.groupAnagrams(case2))
 	print(sol.groupAnagrams(case3))

