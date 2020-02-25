a=[int(i) for i in input().split()]
left=[0]*len(a)
right=[0]*len(a)
left[0]=a[0]
right[-1]=a[-1]
for i in range(1,len(a)):
    if left[i-1]<a[i]:
        left[i]=a[i]
    else:
        left[i]=left[i-1]
#print(left)
for i in range(len(a)-2,-1,-1):
    if right[i+1]<a[i]:
        right[i]=a[i]
    else:
        right[i]=right[i+1]
#print(right)
water=0
for i in range(len(a)):
       water=water+min(left[i],right[i])-a[i]
print(water)
