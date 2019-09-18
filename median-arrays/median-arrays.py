import math

def median_of_two_lists(list1, list2):
  list1Len = len(list1)
  list2Len = len(list2)
  p1 = 0
  p2 = 0
  newList = []

  while (p1 < list1Len or p2 < list2Len):
    if p1 >= list1Len:
      newList.append(list2[p2])
      p2 += 1
      continue
    elif p2 >= list2Len: 
      newList.append(list1[p1])
      p1 += 1
      continue
    
    if list1[p1] < list2[p2] or list1[p1] == list2[p2]:
      newList.append(list1[p1])
      p1 += 1 
    elif list2[p2] < list1[p1]:
      newList.append(list2[p2])
      p2 += 1

  halfLength = int(math.floor(len(newList) / 2))
  if len(newList) % 2 == 0:
    return (newList[halfLength] + newList[halfLength + 1] / 2)
  else:
    return newList[halfLength]

list1 = [2,3,5, 90]
list2 = [2,4,7,20]
print(median_of_two_lists(list1, list2))
