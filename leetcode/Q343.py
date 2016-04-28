class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        else:
            return self.iter(n)

    def iter(self, n):
        if n < 5:
            return n
        else:
            return 3 * self.iter(n - 3)


if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(19))
