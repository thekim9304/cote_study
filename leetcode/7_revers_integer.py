import math

UNDER = math.pow(-2, 31)
UPPER = math.pow(2, 31) - 1

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        if x > 0:
            ret = ''.join(list(str(x))[::-1])
        else:
            nums = list(str(x))[1:]
            nums = nums[::-1]

            ret = '-' + ''.join(nums)

        ret = int(ret)

        if UNDER > ret or UPPER < ret:
            ret = 0

        return ret