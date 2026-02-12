m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mt  = [
      [1,4,7],
      [2,5,8],
      [3,6,9]
]
m90 = [
      [7,4,1],
      [8,5,2],
      [9,6,3]
]

for r in m:
    print (r)
print()
for r in mt:
    print(r)
print()
for r in m90:
    print(r)



























""" def rotate_90_clockwise(matrix):
    n = len(matrix)
    
    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example Usage:
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_90_clockwise(mat)
print(mat) 
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]] """

