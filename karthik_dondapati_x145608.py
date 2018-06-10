import numpy as np
from numpy import matrix,random
from numpy import array

#1.  Include a section with your name

#    Karthik Reddy Dondapati - X145608

#2.  Create matrix A with size (3,5) containing random numbers A = np.random.random(15) 

A=random.random(15)
A=A.reshape(3,5)
A=matrix(A)

#3.  Find the size and length of matrix A 

A.size
A.shape


#4.  Resize (crop/slice) matrix A to size (3,4)
A=np.resize(A,(3,4))

#5.  Find the transpose of matrix A and assign it to B 

B=np.transpose(A)

#6.  Find the minimum value in column 1 of matrix B (check the proper4es of a matrix – ‘B.min()’) 

min(min(B[:,:1]))

#7.  Find the minimum and maximum values for the entire matrix A

np.min(A)
np.max(A)

#8.  Create vector X (an array) with 4 random numbers

X=random.randint(1,45,4)

#9.  Create a func4on and pass vector X and matrix A in it 

from numpy import newaxis
def matrix_multiply(X,A):
    return X*A

#10.  In the new func4on mul4ply vector X with matrix A and assign the result to D 

D=matrix_multiply(X,A)

#11.  Create a complex number Z with absolute and real parts != 0 

Z = np.complex(9,2)

#12.  Show its real and imaginary parts as well as it’s absolute value

np.real(Z)
np.imag(Z)

#13.  Mul4ply result D with the absolute value of Z and record it to C 

ABS=np.absolute(Z)

#14.  Convert matrix B from a matrix to a string and overwrite B 

#print(B.tostring())

B=B.tostring()

#15.  Display a text on the screen: ‘Your Name is done with HW2‘ 

print("Karthik Reddy Dondapati - X145608 is done with Homework 2. Thanks for evaluating Alex") 
