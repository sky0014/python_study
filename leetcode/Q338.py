class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for i in range(num + 1):
            # method 1
            # bit = bin(i).replace('0b','')
            # result.append(int(reduce(lambda x,y:int(x)+int(y),bit)))

            # method 2
            n = 0
            while i > 0:
                n += i & 1
                i = i >> 1
            result.append(n)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(5))
