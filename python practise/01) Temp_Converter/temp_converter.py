def fahrenheit_t0_celcius(f):
    c = (f - 32) * 5/9
    return c

def celcius_to_fahrenheit(c):
    f = c * 9/5 + 32
    return f

def main():
    while True:
        user = input("Press 1 to convert f to c\n press 2 to convert c to f\n press 3 to quit\n >>>> ").strip()
        if user == "1":
            temp = float(input("what is the temperature in fahrenheit? "))
            temp = fahrenheit_t0_celcius(temp)
            print(f"the temperatur in celcius is {temp}")
        elif user == "2":
            temp = float(input("what is the temperature in celcius? "))
            temp = celcius_to_fahrenheit(temp)
            print(f"the temperature in fahrenheit is {temp}")
        elif user == "3":
            break
        else:
            print("invalid choice please try again")

main()