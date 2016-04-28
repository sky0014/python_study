class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        if num < 4:
            return False

        while True:
            if num % 4:
                return False
            else:
                num = num / 4
                if num == 1 or num == 4:
                    return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(16))
