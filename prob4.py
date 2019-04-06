m=int(input())
while m>0:
    n,p=[int(i) for i in input().split()]
    a=(n//2)+1
    b=n%a
    c=p-n
    d=p-b
    if b==0:
        print(d*d*d)
    else:
        print(d*d+d*c+c*c)
    m=m-1
    