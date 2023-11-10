a = int(input())
b = int(input())
c = int(input())

def humor(a,b,c):
    if b < a and c > b:
        return(":)")
    elif b > a and b >= c:
        return(":(")
    elif b > a and c > b:
        if (c-b < b-a):
            return(":(")
        elif (c-b >= b-a):
            return(":)")
    elif(a > b and b < c):
        if(a-b < b-c):
            return(":)")
        elif((a-b >= b-c)):
            return(":(")
    elif(a == b and c > b):
        return(":)")
    elif(a == b and c <= b):
        return(":(")

print(humor(a,b,c))
