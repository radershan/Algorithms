# MergeSort by Radershan

# import infinity for camparing purpose
from decimal import Decimal
a = Decimal('Infinity')

#Main Function 
def MergeSort(A,p,r): # A list to be sort; p,q start & end point of A
    q = (p+r)/2
    if (r-p)>2:
        MergeSort(A,p,q)
        MergeSort(A,q,r)
        return Merge(A,p,q,r)
    else:
        return Merge(A,p,q,r)
    
#Merge function
def Merge(A,p,q,r):
    if r-p>1:
        # Temporarily store A is data for process
        L = A[p:q] 
        L.append(a) #For compare last element
        R = A[q:r]
        R.append(a)
        i = 0
        j = 0
        for k in range(r-p):
            if L[i]<R[j]:
                A[p+k] = L[i]
                i +=1
            else:
                A[p+k] = R[j]
                j +=1
        return A
    else:
        return A

