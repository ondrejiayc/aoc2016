#!/home/ondrej/anaconda3/bin/python

import pandas as pd
import numpy as np

#Problem 1

triangles = np.loadtxt('input.txt')
triDF = pd.DataFrame(triangles, columns=['a','b','c'])
triDF['possible'] = triDF.apply(lambda x: (x.a+x.b>x.c) and (x.b+x.c>x.a) and (x.a+x.c>x.b),axis=1)

print('There are {0} possible triangles (out of {1}) in problem 1.'.format(triDF.possible.sum(),triDF.possible.size))

#Problem 2

triangles = triangles.reshape(-1,triangles.size,order='F').reshape(-1,3)
triDF = pd.DataFrame(triangles, columns=['a','b','c'])
triDF['possible'] = triDF.apply(lambda x: (x.a+x.b>x.c) and (x.b+x.c>x.a) and (x.a+x.c>x.b),axis=1)

print('There are {0} possible triangles (out of {1}) in problem 2.'.format(triDF.possible.sum(),triDF.possible.size))
