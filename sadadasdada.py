a,b = map(int, input().split())
m = [True]*(b+1)
m[0]=m[1]=False
c = 0
for i in range(2,b+1):
    if m[i]:
        if a <= i <=b:
            c+=1
            print(i,end = " ")
        for k in range(i**2,b+1,i):
            m[k]=False
if c ==0:
    print(0)
