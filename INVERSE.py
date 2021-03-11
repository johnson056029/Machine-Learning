#!/usr/bin/env python
# coding: utf-8

import numpy as np
from numpy.linalg import det

def lu_decomp(A_):
    w = np.shape(A_)[0]
    A = np.array(A_)
    for i in range(1,w):
        for j in range(i, w):
            if(A[i-1][i-1] == 0):
                continue
            r = A[j][i-1]*(1.0)/A[i-1][i-1]
            for k in range(i-1, w):
                A[j][k] -= A[i-1][k]*r
            A[j][i-1] = r
    L = np.eye(w) + np.tril(A,k=-1)
    U = np.triu(A)
    return L, U

def rm_rowcol(A, i, j):
    return np.delete(np.delete(A,i,axis=0),j,axis=1)

def cofactor(A,i,j):
    return (-1)**(i+j) * det(rm_rowcol(A,i,j))

def adj(A):
    C = np.empty((A.shape))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            C[i][j] = cofactor(A,i,j) 
    return C.T

def ivrs(A):
    L, U = lu_decomp(A)
    L_inv = adj(L) / det(L)
    U_inv = adj(U) / det(U)
    A_inv = U_inv @ L_inv
    return A_inv