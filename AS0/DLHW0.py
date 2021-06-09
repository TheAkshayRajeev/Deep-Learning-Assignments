#Akshay R, A20442409, CS512, Fall 2020

#!/usr/bin/env python
# coding: utf-8

# In[174]:

#A
import numpy as np
from numpy import linalg as LA
import math as ma
A = np.array([1,2,3])
B = np.array([4,5,6])
C = np.array([-1,1,3])
print(A)
print(B)
print(C)


# In[175]:


#1: 2A − B
print((2*A)-B)     


# In[176]:


#2. ||A|| and the angle of A relative to the positive X axis
normA = LA.norm(A)
normB = LA.norm(B)
xangle = (180/ma.pi)*(ma.acos((A[0])/normA))
print("||A|| = ",normA)
print("angle of A relative to the positive X axis = ",xangle,"degrees")


# In[177]:


#3. a unit vector in the direction of A
print(A/normA)


# In[178]:


#4. the direction cosines of A
cosalpha = (180/ma.pi)*(ma.acos((A[0])/normA))
cosbeta = (180/ma.pi)*(ma.acos((A[1])/normA))
cosgamma = (180/ma.pi)*(ma.acos((A[2])/normA))
print("Direction cosines:")
print("cos A: ",cosalpha, "degrees")
print("cos B: ",cosbeta, "degrees")
print("cos C: ",cosgamma, "degrees")


# In[179]:


#5. A · B and B · A
dot_productAB = np.array(A) @ np.array(B)
dot_productBA = np.array(B) @ np.array(A)
print("A · B = ",dot_productAB)
print("B · A = ",dot_productBA)


# In[180]:


#6. the angle between A and B
angleAB = (180/ma.pi)*ma.acos((dot_productAB)/((normA)*(normB)))
print("the angle between A and B is ",angleAB ,"degrees" )


# In[181]:


#7. a vector which is perpendicular to A
D = np.array([-5,1,1])
dot_productAD = np.array(A) @ np.array(D)
print("D",D,"is a vector which is perpendicular to A since dotprod of A and D = ",dot_productAD)


# In[182]:


#8. A × B and B × A
print("A × B =",np.cross(A,B))
print("B × A =",np.cross(B,A)


# In[183]:


#9. a vector which is perpendicular to both A and B
print(np.cross(A,B)," is a vector perpendicular to A and B")


# In[184]:


#10. the linear dependency between A, B, C
M = np.stack((A, B, C),axis = 1)
print("M = ",M)
print("Determinent(M) = ",np.linalg.det(M))
print("Since Determinent = 0 the vectors are linearly dependent")


# In[185]:


#11. (Atranspose)B and (AB)transpose
print("(Atranspose)B",np.matmul(A.T,B))
print("(AB)transpose",np.multiply.outer(A,B.T))


# In[186]:


#B
A = np.array([[1,2,3],
              [4,-2,3],
              [0,5,-1]])
B = np.array([[1,2,1],
              [2,1,-4],
              [3,-2,1]])
C = np.array([[1,2,3],
              [4,5,6],
              [-1,1,3]])
print(A)
print(B)
print(C)


# In[187]:


#!. 2A − B
print((2*A)-B)


# In[188]:


#2. AB and BA
print("AB = ",np.matmul(A,B))
print("BA = ",np.matmul(B,A))


# In[189]:


#3. (AB)T and BT AT
Z = np.matmul(A,B)
print(Z.T)
print(np.matmul(B.T,A.T))


# In[190]:


#4. |A| and |C| 
print(np.linalg.det(A))
print(np.linalg.det(C))


# In[191]:


#5. the matrix (A, B, or C) in which the row vectors form an orthogonal set
print("In matrix C row vectors form an orthogonal set since determinent of C = 0")


# In[192]:


#6. A−1 and B−1
print("A−1",np.linalg.inv(A))
print("B−1",np.linalg.inv(B))


# In[193]:


#C
A = ([[1,2],
[3,2]])
B = ([[2,-2],
[-2,5]])
print(A)
print(B)


# In[194]:


#1. the eigenvalues and corresponding eigenvectors of A.
value , vector = np.linalg.eig(A)
print("Eigen Values = ", value)
print("Eigen Vectors = ", vector)


# In[195]:


#2. the matrix V−1AV where V is composed of the eigenvectors of A.
value , vector = np.linalg.eig(A)
vector_inv = np.linalg.inv(vector)
X = np.matmul(vector_inv,A)
Y = np.matmul(X,vector)
print(Y)
print("These are the eigen values")


# In[138]:


#3. the dot product between the eigenvectors of A.
value , vector = np.linalg.eig(A)
print(vector)
eigv1, eigv2 = np.atleast_1d(vector)
print(eigv1)
print(eigv2)
print("The dot product between the eigenvectors of A = ", np.dot(eigv1,eigv2))


# In[201]:


#4. the dot product between the eigenvectors of B.
value , vector = np.linalg.eig(B)
print(vector)
eigv1, eigv2 = np.atleast_1d(vector)
print(eigv1)
print(eigv2)
print("The dot product between the eigenvectors of A = ", np.dot(eigv1,eigv2))


# In[135]:


#the property of the eigenvectors of B and its reason
print("Dot product of eigrn vectors of B = 0 which means that the eigen vectors are orthogonal")


# In[199]:


A = ([[-2,3,1],[1,1,2],[10,-5,5]])
print(np.linalg.det(A))


# In[ ]:




