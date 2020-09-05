#Split Array Largest Sum

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low, high = 0, sum(nums)
        while low + 1 < high:
            mid = int(low + (high - low) / 2)
            if self.determinTrue(mid, nums, m):
                high = mid
            else:
                low = mid
        return i if self.determinTrue(low, nums, m) else high

    def determinTrue(self, target, nums, m):
        n = len(nums)
        tmpsum, count = 0, 1
        for num in nums:
            if num > target:
                return False
            if tmpsum + num <= target:
                tmpsum += num
            else:
                tmpsum = num
                count += 1
        return count <= m