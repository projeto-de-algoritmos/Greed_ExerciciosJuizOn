# 330. PETCHING ARRAY - HARD
# https://leetcode.com/problems/patching-array/

class Solution(object):
    def minPatches(self, nums, n):
        miss = 1  # Initialize miss to 1
        patches = 0  # Initialize the number of patches required
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]  # Extend the range to include nums[i]
                i += 1
            else:
                miss += miss  # Add the miss value to the array and update the range
                patches += 1  # Increment the patch count

        return patches

# Example usage:
solution = Solution()

# Example 1
nums = [1, 3]
n = 6
print(solution.minPatches(nums, n))  # Output: 1