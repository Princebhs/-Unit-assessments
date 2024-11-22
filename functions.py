def temperature_converter():

    print("Choose conversion type: ")
    print("1: Celsius to Fahrenheit. ")
    print("2: Fahrenheit to Celsuis. ")

Number = input("enter number (1 or 2):")


if Number == "1":
       celsius = float(input("Enter temperature in Celsius: "))
       fahrenheit = (celsius * 9/5) + 32
       print(f"{celsius} C = {fahrenheit:.2f} F") 

elif Number == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celsius = (fahrenheit - 32) * 9/5
    print(f"{fahrenheit}°F = {Celsius:.2f}°C") 

else:
       print("Invalid choice. Please enter 1 or 2.")

temperature_converter()
   






    
    




   
