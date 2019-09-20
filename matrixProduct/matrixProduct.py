
def find_best_product(matrix):
  leng = len(matrix)
  max_sum = -1

  def find_best_path(x, y, sumVal):
    print(x, y, sumVal)
    if(x >= leng or y >= leng):
      return

    if(x == leng - 1 and y == leng - 1):
      nonlocal max_sum
      sumVal *= matrix[x][y]
      max_sum = max(max_sum, sumVal)
      return 

    sumVal *= matrix[x][y]
    find_best_path(x, y + 1, sumVal)
    find_best_path(x + 1, y, sumVal)
  
  find_best_path(0, 0, 1)
  print(max_sum)
  return max_sum

test_matrix_1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

test_matrix_2 = [
  [-1,2,3],
  [4,5,-6],
  [7,8,9]
]

find_best_product(test_matrix_1)
find_best_product(test_matrix_2)
