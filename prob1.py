for i in range(int(input())):
    string=input()
    flag=0
    splitter=string.split(" ")
    for j in range(len(splitter)):
        if splitter[j]=="not":
            flag=1
            break
    if flag==0:
        print("regularly fancy")
    else:
        print("Real Fancy")