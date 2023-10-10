def Linear_Search_Product(inpt,*n):
    j=0
    k=0
    s=[]
    for i in n:
        j=j+1
    for i in range(j):
        if n[i]==inpt:
            s.append(i)
            k=k+1
    return s

s=[]

n=int(input("Enter no.of numbers :"))
print("Enter ur List :")

for i in range(n):
    print(i+1,':',end='')
    s.append(int(input()))

print(Linear_Search_Product(int(input("\nEnter a no. in list to Search:")),*s))
