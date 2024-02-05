"""
You are given a 0-indexed integer array nums and an integer k.
You are initially standing at index 0. In one move, 
you can jump at most k steps forward without going outside the boundaries of the array. 
That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
You want to reach the last index of the array (index n - 1). 
Your score is the sum of all nums[j] for each index j you visited in the array.
Return the maximum score you can get.
"""
class Solution(object):
    def maxResult(self, nums, k):
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        queue = deque([0])
        for idx in range(1, length):
            while queue and queue[0] < idx - k:
                queue.popleft()
            dp[idx] = dp[queue[0]] + nums[idx]
            while queue and dp[queue[-1]] <= dp[idx]:
                queue.pop()
            queue.append(idx)
        return dp[length-1]
