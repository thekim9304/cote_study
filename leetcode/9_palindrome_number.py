class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x_str = str(x)

        res = True
        front_idx = 0
        for back_idx in range(len(x_str) - 1, 0, -1):
            if x_str[front_idx] != x_str[back_idx]:
                res = False
                break

            front_idx += 1
        return res