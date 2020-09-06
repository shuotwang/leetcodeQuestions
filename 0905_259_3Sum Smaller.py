class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        #         def twoSumSmaller(idx: int, target: int) -> int:
        #             ans = 0
        #             for i in range(idx, len(nums) - 1):
        #                 j = bisect_left(nums, target - nums[i], i + 1) - 1
        #                 ans += j - i
        #             return ans

        #         nums.sort()
        #         ans = 0
        #         for i in range(len(nums) - 2):
        #             ans += twoSumSmaller(i + 1, target - nums[i])

        #         return ans

        def twoSumSmaller(idx: int, target: int) -> int:
            ans = 0
            l, r = idx, len(nums) - 1
            while l < r:
                summ = nums[l] + nums[r]
                if summ < target:
                    ans += r - l
                    l += 1
                else:
                    r -= 1
            return ans

        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            ans += twoSumSmaller(i + 1, target - nums[i])
        return ans