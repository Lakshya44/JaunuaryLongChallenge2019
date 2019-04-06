# cook your dish here
t=int(input())
while t>0:
    n,a,b=[int(i) for i in input().split()]
    arr=[int(i) for i in input().split()]
    both=0
    alice=0
    bob=0
    for i in range(n):
        if arr[i]%a==0 and arr[i]%b==0:
            both=1
        elif arr[i]%a==0:
            bob+=1
        elif arr[i]%b==0:
            alice+=1
    if both==1:
        if bob>=alice:
            print("BOB")
        else:
            print("ALICE")
    else:
        if bob>alice:
            print("BOB")
        else:
            print("ALICE")
    t=t-1
            
