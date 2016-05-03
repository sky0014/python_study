from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        return sorted(c, key=c.get, reverse=True)[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([2, 2, 1, 1, 1, 3, 3, 2, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3], 2))
