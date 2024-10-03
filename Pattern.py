def ptrn1(n):
    for i in range(0,n+1):
        for j in range(i):
            print("*", end="")
        print()
def ptrn2(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end="")
        print()
    
            
n = int(input())           
operator = int(input())
match operator:
    case 1: ptrn1(n)
    case 0: ptrn2(n)
    
