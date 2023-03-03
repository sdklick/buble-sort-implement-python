#buble sort implementation in python

a=[]
usernumber=int(input('how much element you Enter : '))
for z in range(usernumber):
    userinput=int(input('please enter value : '))
    a.append(userinput)
print(f'First list : {a}')
for i in range(0,len(a)):
    for x in range(len(a)-i-1):
        if a[x]>a[x+1]:
            b=a[x]
            a[x]=a[x+1]
            a[x+1]=b
print(f'afer sorting : {a}')            