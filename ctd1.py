x=str(input("enter (1) if celsius enter (2) if fahrenheit  "))
if x == '1' :
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
elif x == '2' :
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))
else:
    print("error enter valid input")
