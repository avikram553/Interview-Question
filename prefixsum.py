a=[int(i) for i in input().split()]
psum=[0]*len(a)
psum[0]=a[0]
for i in range(1,len(a)):
    psum[i]=psum[i-1]+a[i]
for i in range(len(a)):
    lsum=psum[i]-a[i]
    rsum=psum[len(a)-1]-psum[i]
    if lsum==rsum:
        bool=True
        d=a[i]
        break
    else:
        bool=False
if bool:
    print('YES',d)
else:
    print('NO')
    
