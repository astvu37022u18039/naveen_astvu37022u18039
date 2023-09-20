def fact(n):
    if(n>1): return(n*fact(n-1))
    else: return(1)

n=int(input("Enter n value : "))
print("Factorial of ",n," is ",fact(n))
input()