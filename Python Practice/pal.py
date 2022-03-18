# reversing a number using divmod
num = 132
pal = 0
while num!=0:
    use = divmod(num, 10)
    dig = use[1]
    pal = pal*10+dig
    num = use[0]
print(use)