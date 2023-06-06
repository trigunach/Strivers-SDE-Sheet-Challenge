#Approach : Dutch National Flag algorithm
def sortColors(arr , n):
  low = 0
  high = n-1
  i = 0
  while i <= high:
      if arr[i] == 0:
          arr[low],arr[i] = arr[i],arr[low]
          low += 1
          i += 1
      elif arr[i] == 2:
          arr[high],arr[i] = arr[i],arr[high]
          high -= 1
      else:
          i += 1
  return arr
