class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, present_len = 0, 0
        length = len(s)
        start, end = 0, 0
        s_set = set()
        while end < length:
            # print(f"{s[start:end+1]}")
            if s[end] not in s_set:
                s_set.add(s[end])
                end += 1
                present_len += 1
            else:
                s_set.remove(s[start])
                start += 1
                present_len -= 1
            
            if max_len < present_len:
                max_len = present_len
        
        return max_len