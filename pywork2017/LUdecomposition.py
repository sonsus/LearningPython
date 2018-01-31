'''Solving Ax=B with LUfactorization and backsubstitution'''
#shorcut method:  https://www.youtube.com/watch?v=UlWcofkUDDU
#step by step  :  https://www.youtube.com/watch?v=rhNKncraJMk

import numpy as np

#B=np.asarray( A )  : copy=False --> pass by reference  --> modifying A will affect B 
#B=np.array( A )    : copy=True  --> pass by value      --> A and B are different instances
# A : array like obj
# np.matmul() != np.dot() : different broadcasting rule for tensors 


#L is lower triangular matrix with diagonal 1
#U is upper triangular matrix with variable diagonal 
def LUdecompose(Amat):
    A=np.array(Amat) #list --> np.array
    len_mat=len(Amat[0])
    L=np.identity(len_mat) #init L and U
    U=A

    for col in range(len_mat):
        for row in range(col+1, len_mat):
            c=U[row][col]/U[col][col]
            L[row][col]=c
            U[row]=U[row]-c*U[col]
    return L, U

def Back_sub(L,U,B_vec):
    #Ax=LUx=B
    #Ux=y  --> x= U- *y
    #Ly=B  --> y= L- *B
    B=np.array(B_vec)
    invL=np.linalg.inv(L)
    invU=np.linalg.inv(U)
    y=np.matmul(invL,B)
    x=np.matmul(invU,y)
    return x


if __name__=="__main__":
    A_matrix=[ #compatible with any square-matrices
             [ 1, 3, 2, 5, 2],
             [ 2, 3, 4,-3, 2],
             [ 3, 4,-3, 2, 0],
             [-1,-2,-3, 4, 2],
             [ 6, 9, 8, 2, 1]
            ]

    B_vec=[6,2,16,2,3]

    #L,U=LUdecompose(A_matrix)
    x=Back_sub(LUdecompose(A_matrix),B_vec)    

    print("solving Ax=B")
    print("A = \n", np.array(A_matrix))
    print("B = \n", np.array(B_vec))
    print("A = LU")
    print("L = \n", L)
    print("U = \n", U)
    print("\nThus x is\n", x)



#thinking raw (implementation of LUdecompose function)

#trial 1: erase first column of u0 with u[0][0]-->u1 obtained 
#trial 2: erase second column with u1[1][1]-->u2 obtained
#trial 3: erase thrid column with u2[2][2]-->u3 obtained
#trial 4: erase fourth column with u3[3][3]-->u4 obtained
#(trial ends in len(p[0])-1 th turn)