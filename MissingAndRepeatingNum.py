def missingAndRepeating(arr, n):
  # Write your code here
  hash = [0]*(n+1)
  for i in range(n):
      hash[arr[i]] += 1 
  repeating, missing = -1, -1
  for i in range(1, n + 1):
      if hash[i] == 2:
          repeating = i
      elif hash[i] == 0:
          missing = i

      if repeating != -1 and missing != -1:
          break
  return [ missing , repeating]
