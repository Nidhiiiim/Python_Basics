from self import self


class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        length = len(x_str)
        for i in range(length // 2):
            if x_str[i] != x_str[length - i - 1]:
                print("False")
                return False
        print("True")
        return True


x = input("Provide the number: ")
Solution.isPalindrome(self, x)
