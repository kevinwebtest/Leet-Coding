def solution(K, A): #O(N**2)
    count = 0
    out= []
    for i in range(len(A)):
        for j in range(i+1, len(A)+1):
            maxx = max(A[i:j])
            minn = min(A[i:j])
            if maxx-minn<=K:
                count+=1
                out.append((i,j-1))
    return count

def solution(A):  #O(NlogN)
    count = 0
    if len(A)>1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]

        count += solution(L)
        count += solution(R)

        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                A[k] = L[i]
                i+=1
            else:
                count += len(L)-i
                if count>1_000_000_000:
                    return -1
                A[k] = R[j]
                j+=1
            k+=1
        while i<len(L):
            A[k] = L[i]
            i+=1
            k+=1
        while j<len(R):
            A[k] = R[j]
            j+=1
            k+=1
    
    return count