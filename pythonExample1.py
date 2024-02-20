#!/usr/bin/env python3


matrix=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

factor      =len(matrix)**2

top_is      =0
left_is     =0
right_is    =len(matrix)-1
bottom_is   =len(matrix)-1

top         =len(matrix)
right       =len(matrix)
bottom      =len(matrix)-2
left        =len(matrix)-2
z           =[]

while factor>0:
    for i in range(top):
        z.append(matrix[top_is][i])
        factor=factor-1

    top=top-1
    top_is=top_is+1

    for j in range(1,right):
        z.append(matrix[j][right_is])
        factor=factor-1

    right_is=right_is-1
    right=right-1

    for k in range(bottom,-1,-1):
        z.append(matrix[bottom_is][k])
        factor=factor-1

    bottom=bottom-1
    bottom_is=bottom_is-1

    for s in range(left,left_is,-1):
        z.append(matrix[s][left_is])
        factor=factor-1

    left_is=left_is+1
    bottom_is=top_is

print(z)
