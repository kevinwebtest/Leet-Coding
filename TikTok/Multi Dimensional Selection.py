def getMaxProduct(arr):
    n = len(arr)
    m = len(arr[0])
    a = []
    req = (m+1)//2
    curr = [0]*n
    for i in range(n):
        for j in range(m):
            a.append([arr[i][j],i])

    a.sort()
    ok, mxx, ans, i, j = 0, 0, 10**9, 0, 0
    while i<len(a):
        while j<len(a) and ok!=n:
            curr[a[j][1]]+=1
            if curr[a[j][1]]==req:
                ok+=1
            j+=1

        if ok==n:
            ch = a[j-1][0]
            while j<len(a) and a[j][0]==ch:
                curr[a[j][1]]+=1
                if curr[a[j][1]]==req:
                    ok+=1
                j+=1
            if a[j-1][0]-a[i][0] < ans:
                ans = a[j-1][0]-a[i][0]
                mxx = j-i
            elif a[j-1][0]-a[i][0] == ans:
                mxx = max(mxx,j-i)

        curr[a[i][1]]-=1
        if curr[a[i][1]]==req-1:
            ok-=1
        i+=1
    return ans*mxx

print(getMaxProduct([[2, 3], [1, 2], [4, 3]]))
print(getMaxProduct([[1, 4, 3], [3, 5, 6]]))
