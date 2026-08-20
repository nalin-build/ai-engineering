def add_score(grades, name, score):
    if name in grades:
        grades[name].append(score)
    else:
        grades[name] = [score]

def average_score(grades, name):
    score = grades[name]
    return sum(score) / len(score)

    




def main():
    grades = {}
    while True:
        name = input("please enter a name or type done to exit: ").lower()
        if name == "done":
            break
        else:
            score = input("please enter the score: ")
            try:
                score = float(score)
                add_score(grades, name, score)
            except ValueError:
                print("please input a valid score ")

    for name in grades:
        average = average_score(grades, name )
        print(f"{name} has an average of {average:.2f}")








main()