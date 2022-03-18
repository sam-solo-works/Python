age = input("How old are you?\n")

agelist = [int(d) for d in str(age)]
centuries = agelist[0]
decades = agelist[1]
years = agelist[2]

if centuries > 0:
    if centuries == 1:
        print("You are " + str(centuries) + " century, " + str(decades) + " decades, and " + str(years) + " years old.")
    else:
        print("You are " + str(centuries) + " centuries, " + str(decades) + " decades, and " + str(years) + " years old.")
else:
    print("You are " + str(decades) + " decades, and " + str(years) + " years old.")

    