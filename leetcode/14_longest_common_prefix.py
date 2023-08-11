class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_len_lst = [len(_str) for _str in strs]

        max_len = max(str_len_lst)

        max_prefix = ''

        if len(str_len_lst) == 1:
            max_prefix = strs[0]
        else:
            for i in range(1, max_len + 1):
                prefix = strs[0][:i]
                check = True

                for _str in strs[1:]:
                    if prefix != _str[:i]:
                        check = False

                        break

                if check:
                    max_prefix = prefix

        return max_prefix
