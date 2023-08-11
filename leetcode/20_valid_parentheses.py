class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        res = True
        if len(s) == 1:
            res = False
        else:
            for elem in s:
                if elem == ')':
                    if len(stack) == 0:
                        res = False
                        break
                    if stack and stack.pop() != '(':
                        res = False
                        break
                elif elem == ']':
                    if len(stack) == 0:
                        res = False
                        break
                    if stack and stack.pop() != '[':
                        res = False
                        break
                elif elem == '}':
                    if len(stack) == 0:
                        res = False
                        break
                    if stack and stack.pop() != '{':
                        res = False
                        break
                else:
                    stack.append(elem)

        if len(stack) > 0:
            res = False

        return res