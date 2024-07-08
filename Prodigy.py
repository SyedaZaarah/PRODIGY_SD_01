try:
    value = input("Temperature Value:  ")
    value = int(value)
    unit = input("Enter Unit (C)elsius, (F)ahrenheit, or (K)elvin:  ")
    unit = unit.upper()
except ValueError:
    print("Invalid Value")


if unit == "C":
    C_to_F = (value * 9/5) + 32
    print(f"Temperature in Fahrenheit is {C_to_F}")
    C_to_K = value + 273.15
    print(f"Temperature in Kelvin is {C_to_K}")

if unit == "F":
    F_to_C = (value - 30) / 2
    print(f"Temperature in Celsius is {F_to_C}")
    F_to_K = (value - 32) * 5 / 9 + 273.15
    print(f"Temperature in Kelvin is {F_to_K}")

if unit == "K":
    K_to_C = value - 273.15
    print(f"Temperature in Celsius is {K_to_C}")
    K_to_F = (value - 273.15) * 9/5 + 32
    print(f"Temperature in Farenheit is {K_to_F}")
