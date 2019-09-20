
def find_best_product(matrix):
  leng = len(matrix)
  max_product = -1

  def find_best_path(x, y, productVal):
    if(x >= leng or y >= leng):
      return

    if(x == leng - 1 and y == leng - 1):
      nonlocal max_product
      productVal *= matrix[x][y]
      max_product = max(max_product, productVal)
      return 

    productVal *= matrix[x][y]
    find_best_path(x, y + 1, productVal)
    find_best_path(x + 1, y, productVal)
  
  find_best_path(0, 0, 1)
  return max_product

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
