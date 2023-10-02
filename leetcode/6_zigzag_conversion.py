class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            ret = s
        else:
            baskets = [[] for _ in range(numRows)]

            idx = 0
            add_num = -1
            i = 0
            while i < len(s):
                if idx == 0:
                    add_num *= -1
                elif idx == (numRows - 1):
                    add_num *= -1

                baskets[idx].append(s[i])

                idx += add_num
                i += 1

            ret = ''
            for basket in baskets:
                ret += ''.join(basket)

        return ret