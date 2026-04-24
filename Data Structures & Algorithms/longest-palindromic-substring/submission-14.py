class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        ans = s[0]
        for center in range(1, len(s)):
            tmp = ''
            for i in range(1, center+1):
                if center+i >= len(s):
                    break
                if s[center-i] == s[center+i]:
                    tmp = s[center-i:center+i+1]
                    if len(tmp) > len(ans):
                        ans = tmp
                else:
                    break

        
        res = s[0]
        for center in range(0, len(s)):
            tmp = ''
            for i in range(1, center+2):
                if center+i >= len(s):
                    break
                if s[center-(i-1)] == s[center+i]:
                    tmp = s[center-(i-1):center+i+1]
                    if len(tmp) > len(res):
                        res = tmp
                else:
                    break
        
        print(len(ans), len(res))
        if len(res) > len(ans):
            return res
        else:
            return ans



