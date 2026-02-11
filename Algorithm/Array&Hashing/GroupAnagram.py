from typing import List     
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            key_map = ''.join(sorted(s))
            if key_map not in anagram_map:
                anagram_map[key_map] = [s]

            else: 
                anagram_map[key_map].append(s)
        return list(anagram_map.values())


        



if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


    solution = Solution()
    print(solution.groupAnagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]