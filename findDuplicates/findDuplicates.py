def find_duplicates(arr):
  dictionary = {}
  nums = []
  for i in arr:
   if i in dictionary: 
     nums.append(i)
   else:
    dictionary[i] = True
  return nums

find_duplicates([1,2,4,3,4,5,6,7,7])