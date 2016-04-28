class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aoieu'
        rs = [c for c in s if c.lower() in vowels][::-1]
        result = [rs.pop(0) if c.lower() in vowels else c for c in s]
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels('leEtcOde'))
