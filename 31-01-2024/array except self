'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]'''

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [1] * n  # prefix product
    suffix = [1] * n  # suffix product

    for i in range(1, n):
      prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in reversed(range(n - 1)):
      suffix[i] = suffix[i + 1] * nums[i + 1]

    return [prefix[i] * suffix[i] for i in range(n)]
