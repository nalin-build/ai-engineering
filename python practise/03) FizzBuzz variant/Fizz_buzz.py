def get_int_values(label):
    while True:
        value = input(f"{label} please type in the number: ")
        try:
            value = int(value)
            return value
        except ValueError:
            print("please input a valid number: ")
            





def main():
    while True:
        start_num = get_int_values("To start")
        end_num = get_int_values("To end")
        if start_num < end_num:
            break
        else:
            print("please input a valid range with the ending number being greater than the starting")

    for i in range(start_num, end_num + 1):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
                print(i)








main()