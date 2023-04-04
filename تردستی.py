inp=int(input())


lst=[]
for i in range(0,inp):
    n=input()
    time=0
    d=True
    for i in n:
        if i=='0' and d==True:
            time+=1
            d=False
        if i=='1':
            d=True
    lst.append(time)


    
print(*lst,sep = "\n")
