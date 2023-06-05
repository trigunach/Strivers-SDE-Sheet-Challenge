def nextPermutation(nums):
  if nums == sorted(nums)[::-1]:
      nums.sort()
  else:
      n = len(nums)
      idx = -1
      for i in range(n-2,-1,-1):
          if nums[i] < nums[i+1]:
              idx = i 
              break 
      if idx == -1:
          nums.reverse()
      for i in range(n-1,idx,-1):
          if nums[i] > nums[idx]:
              nums[i],nums[idx] = nums[idx],nums[i]
              break
      nums[idx+1:] = reversed(nums[idx+1:])
  return nums
