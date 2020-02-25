a=[int(i) for i in input().split()]
k=int(input())
n=len(a)
psum=[0]*n
psum[0]=a[0]
for i in range(1,n):
    psum[i]=psum[i-1]+a[i]
    current=0;maxi=-1000000;
for i in range(n):
    if i==k-1:
        current=psum[i]
        maxi=max(current,maxi)
    elif i>k-1:
        current=psum[i]-psum[i-k]
        maxi=max(current,maxi)
print(maxi)
        
    
