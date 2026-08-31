import csv


def main():
    grades = {}
    file_name = input("please enter the file name wihtout .csv : ").strip()
    file_name = file_name + '.csv'
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0].strip()
                score = float(row[1].strip())
                grades[name] = score
    except FileNotFoundError:
        print("no existing file found, starting fresh")


    while True:
        name = input("enter a name, or 'done' to finish: ").strip().lower()
        if name == "done":
            break
        if name in grades:
            change = input(f"{name} already has a score, edit it? y/n: ").strip().lower()
            if change != 'y':
                continue
    
        while True:
            try:
                score = float(input("enter score: "))
                if score <= 100:
                    grades[name] = score
                    break
                else:
                    print("please enter a valid grade")
            except ValueError:
                print("please enter a valid grade")





    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        for name, score in grades.items():
            writer.writerow([name, score])


main()