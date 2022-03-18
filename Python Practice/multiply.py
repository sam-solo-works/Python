s, n = input("Enter 2 numbers to multiply:\n").split()
s = int(s)
n = int(n)

def multiply(s,n):
    return s*n

print(s," times ",n," equals ",multiply(s,n),".", end = "")