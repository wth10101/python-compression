m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mrs = [
      [7, 8, 9],
      [4, 5, 6],
      [1, 2, 3]
]

m180 = [  # reverse each row
       [9,8,7],
       [6,5,4],
       [3,2,1]
]





""" #swap rows
mrs = []
for i in range(len(m)-1,-1,-1):
    mrs.append(m[i])

#reverse each row
for r in range(len(mrs)):
    mrs[r].reverse()

for r in mrs:
    print(r) """