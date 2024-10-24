class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        long = len(nums)
        answer = 0

        for i in range(long - 2):
            for j in range(i + 1, long - 1):
                if nums[i] != nums[j]:
                    for k in range(j + 1, long):
                        if nums[k] != nums[i] and nums[k] != nums[j]:
                            answer += 1

        return answer
