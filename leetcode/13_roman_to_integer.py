class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_val_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, '1': 4, '2': 9, '3': 40,
                           '4': 90, '5': 400, '6': 900}

        s = s.replace('IV', '1')
        s = s.replace('IX', '2')
        s = s.replace('XL', '3')
        s = s.replace('XC', '4')
        s = s.replace('CD', '5')
        s = s.replace('CM', '6')

        res = 0
        for symbol in s:
            res += symbol_val_dict[symbol]

        return res