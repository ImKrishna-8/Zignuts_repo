def cel_to_feh(celsi):
    return (celsi * 9/5) + 32

celsi = int(input("Enter Temperature in Celsius: "))
print("Temperature in Fahrenheit is:", cel_to_feh(celsi))

