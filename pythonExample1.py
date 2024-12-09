#!/usr/bin/env python3


# matrix=[ [1,2,3], [4,5,6], [7,8,9] ]
a=5
matrix = [ list(range(i*a+1, (i+1)*a+1)) for i in range(a) ]


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
    print(f'FACTOR BEGIN:={factor}')
    for i in range(top):
        z.append(matrix[top_is][i])
        factor-=1

    top-=1
    top_is+=1
    print(f'Z:= {z}')

    for i in range(1,right):
        z.append(matrix[i][right_is])
        factor-=1

    right_is-=1
    right-=1
    print(f'Z:= {z}')

    for i in range(bottom,-1,-1):
        z.append(matrix[bottom_is][i])
        factor-=1

    bottom-=1
    bottom_is-=1
    print(f'Z:= {z}')

    for i in range(left,left_is,-1):
        z.append(matrix[i][left_is])
        factor-=1

    left_is+=1
    bottom_is=top_is
    print(f'FACTOR END:={factor}')


print(z)
