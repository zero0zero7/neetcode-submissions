class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        base = [0]*26
        word = strs[0]
        for char in word:
            base[ord(char) - ord('a')] += 1
        base_count = {str(base): [word]}

        for word in strs[1:]:
            base = [0]*26
            for char in word:
                base[ord(char) - ord('a')] += 1
            if str(base) in base_count.keys():
                base_count[str(base)].append(word)
            else:
                base_count[str(base)]= [word]
        return list(base_count.values())