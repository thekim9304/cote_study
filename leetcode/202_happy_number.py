class Solution:
    def isHappy(self, n: int) -> bool:
        ret = True
        checked_lst = [n]
        while n != 1:
            n_lst = list(str(n))

            n_lst = [int(_n) * int(_n) for _n in n_lst]

            n = sum(n_lst)

            if n in checked_lst:
                ret = False
                break
            else:
                checked_lst.append(n)

        return ret