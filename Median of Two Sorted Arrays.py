#Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)  # 合并排序
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]


if __name__ == '__main__':
    nums1, nums2 = [1, 3], [3, 4]
    solu = Solution()
    print(solu.findMedianSortedArrays(nums1, nums2))