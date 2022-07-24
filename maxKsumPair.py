class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        cnt = 0
        while left < right :
            if nums[right] + nums[left] == k :
                left +=1
                right -=1
                cnt +=1
            elif nums[right] + nums[left] > k :
                right -=1
            elif nums[right] + nums[left] < k :
                left +=1
        return cnt
