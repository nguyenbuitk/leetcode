# I think a good explanation for why we move pointer with the lower height is because we already have the max area with that height - since it is the lower pointer that means that every other area that is closer will always be a smaller distance with the same or less height which means smaller area. 
# Therefore we do not need to look at every other combination with that pointer.
class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    res = 0
    while left < right:
      res = max(res, (right - left)*min(height[right], height[left]))
      if height[left] <= height[right]:
        left += 1
      else: right -= 1
    return res

solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
