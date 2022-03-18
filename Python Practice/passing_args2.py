def replace(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g =", g) #must use object reference to pass replace arguments in f

f = [14, 23, 37]
replace(f)
print("f = ", f)