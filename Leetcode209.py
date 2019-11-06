class Solution(object):
    """
            :type s: int
            :type nums: List[int]
            :rtype: int
            """

    def minSubArrayLenOn(self, s, nums):
        total = left = 0;
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0

    def minSubArrayLenOnlogn(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left

if __name__=="__main__":
    solution=Solution()
    print(solution.minSubArrayLenOnlogn(7,[2,3,1,2,4,3]))
