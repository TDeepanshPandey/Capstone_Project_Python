def mass_convert(w: int):
    return w*100


def temp_convert(t: int):
    pass


if __name__ == "__main__":
    unit = int(input("Enter your choice for conversion: \n 1. Temp \n 2. Mass \n"))
    if unit == 2:
        weight = int(input("Enter the weight in kgs : "))
        print("Mass in grams", mass_convert(weight))
    if unit == 1:
        temp = int(input("Enter temperature in Celsius : "))
        print("Temperature in Fahrenheit : ", temp_convert(temp))
