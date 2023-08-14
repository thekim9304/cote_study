class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length

# Time Out
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#
#         back_idx = 1
#         longest_len = 0
#         longest_str = ''
#         for front_idx in range(len(s) - 1):
#             for back_idx in range(front_idx, len(s) + 1, 1):
#                 sub_str = s[front_idx:back_idx]
#                 unq_s = ''.join(dict.fromkeys(sub_str))
#
#                 ori_len = len(s[front_idx:back_idx])
#                 unq_len = len(unq_s)
#
#                 if ori_len == unq_len:
#                     if ori_len > longest_len:
#                         longest_len = ori_len
#                         longest_str = sub_str
#                 else:
#                     break
#
#         if len(s) == 1:
#             longest_len = 1
#
#         return longest_len