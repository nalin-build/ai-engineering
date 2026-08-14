def max_number(numbers):
    
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest

def min_number(numbers):

    lowest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < lowest:
            lowest = numbers[i]
    return lowest


def num_average(numbers):
    
   
    total = 0
    for i in range(len(numbers)):           
        total += numbers[i]
    average = total / float(len(numbers))
    return average
 


def main():
    numbers = []
    while True:
        user_input = input("please type in the number you would like to add to the list or type done to exit:  ").strip().lower()
        if user_input == 'done':
            break
        else:
            try:
                value = float(user_input)
                numbers.append(value)
            except ValueError:
                print("please input a valid number ")
    if len(numbers) == 0:
                print("no numbers were added")
                return

    maximum = max_number(numbers)
    minimum = min_number(numbers)
    average = num_average(numbers)

    print(f"The maximum number is: {maximum}\n The minimum number is: {minimum}\n The average is: {average}")



main()

