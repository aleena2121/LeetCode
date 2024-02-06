class Solution(object):
    def groupAnagrams(self, words):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = {}
        
        for word in words:
            key = "".join(sorted(word))
            
            if key not in anagram_groups:
                anagram_groups[key] = [word]
            else:
                anagram_groups[key].append(word)
        
        return anagram_groups.values()