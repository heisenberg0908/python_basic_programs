
X=[
    [1,2,3],
    [2,3,4],
    [45,6,7]
]
Y=[
    [3,6,8],
    [9,8,7],
    [4,6,9]
]
Z=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
# addition of 2 matrice
for i in range(len(X)):
    for j in range(len(X[0])):
        Z[i][j]=X[i][j]+Y[i][j]
print(Z)
# subtarction of 2 matrice:
for i in range(len(X)):
    for j in range(len(X[0])):
        Z[i][j]=X[i][j]-Y[i][j]
print(Z)
# multiplication of 2 matrices:
for i in range(len(X)): 
    for j in range(len(X[0])):
        Z[i][j]=X[i][j]*Y[i][j]
print(Z)
# transpose of a matrice:
P=[
    [1,2,3],
    [4,5,6]
]
for i in range(100):
    
        


        