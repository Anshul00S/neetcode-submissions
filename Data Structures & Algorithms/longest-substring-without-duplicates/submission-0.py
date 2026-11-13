class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        
        maxLen = 0

        l = 0 
        r = 0

        while r < len(s):
            if s[r] in chars:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1

            chars.add(s[r]) 
            maxLen = max(maxLen, len(chars))
            r+= 1

        return maxLen





        