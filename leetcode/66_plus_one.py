class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        return [int(digit) for digit in str(int(''.join(digits)) + 1)]