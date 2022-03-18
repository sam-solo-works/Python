Temperature = 95
Forecast = "sunny"

if Temperature > 80 and Forecast != "rain":
    print("It's too hot!")
    print("Stay inside!")
elif Temperature < 60 and Forecast != "sunny":
    print("It's too cold!")
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")
#print("Have a good day!")