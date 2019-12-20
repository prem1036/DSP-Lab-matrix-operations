#operation on matrices
import numpy as np
a=int(input("enter the number of rows\n"))	#Number of rows
b=int(input("enter the number of columns\n"))	#Number of columns
n=[]
for i in range(a):
	n.append([0]*b)
for i in range(a):
	for j in range(b):
		print("enter the elements into matrix::",[i,j]) #it shows the index of matrix
		n[i][j]=int(input())
print("the entered matrix is "),
print(np.matrix(n))	#given matrix
if a==b:
	print("determinant of given matrix is:") 	#determinant of given matrix
	print(np.linalg.det(n),"\n")
	print("trace of given matrix is")	
	print(np.trace(n),"\n")		#Trace of given matrix
else:
	print("for determinant & trace enter matrix which have equal no.of rows and columns")
print("transpose of agiven matrix is:"),
print(np.transpose(n),"\n")		#transpose of given matrix
print("Rank of the  given matrix is:")
print(np.linalg.matrix_rank(n),"\n") 	#rank of given matrix
print("inverse of the given matrix is")	
print(np.linalg.inv(n),"\n")		#inverse of given matrix
print("eigen values of the given matrix is:")
print(np.linalg.eigvals(n),"\n") 	#eigen values of given matrix
p=int(input("enter the power of matrix"))
print(np.linalg.matrix_power(n,p),"\n")  #finding power for given matrix 
print("norm of the given matrix")
print(np.linalg.norm(n),"\n")	#matrix norm of given matrix
print("pseudo inverse of  given matrix ")
print(np.linalg.pinv(n),"\n")	#pseudo inverse of given matrix 

