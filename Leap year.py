def isLeap(n):
    if((n%4==0 and n%100!=0) or n%400==0): return 1
    else: return 0

if(isLeap(int(input("Enter a Year : ")))): print("It is a Leap Year")
else: print("It is not a Leap Year ")

input()