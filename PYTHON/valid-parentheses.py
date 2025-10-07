class Solution:
    def is_matching(self, a, b):
        # Function to check if the pair of brackets match
        return (a == '(' and b == ')' or
                a == '[' and b == ']' or
                a == '{' and b == '}')

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                if self.is_matching(stack[-1], char):
                    stack.pop()
                else:
                    return False

        return not stack 

if __name__ == "__main__":
    sol = Solution()
    s = input("Enter a string of brackets: ")
    if sol.isValid(s):
        print("The string is valid.")
    else:
        print("The string is not valid.")
