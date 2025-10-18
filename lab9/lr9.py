import os

FILENAME = "students.txt"

def create_file():
    students = [
        ("Іваненко Іван", 82),
        ("Петренко Петро", 91),
        ("Коваль Олег", 75),
        ("Мельник Марія", 88)
    ]
    with open(FILENAME, "w", encoding="utf-8") as f:
        for name, score in students:
            f.write(f"{name};{score}\n")
    print("Файл створено!")

def read_file():
    if not os.path.exists(FILENAME):
        print("Файл не знайдено!")
        return
    with open(FILENAME, "r", encoding="utf-8") as f:
        print("Вміст файлу:")
        print(f.read())

def write_file():
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write("Новий Студент;95\n")
    print("Дані перезаписані!")

def append_file():
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write("Додатковий Студент;77\n")
    print("Дані дозаписані!")

def search_file(filename):
    files = os.listdir(".")
    if filename in files:
        print(f"Файл {filename} знайдено в каталозі.")
    else:
        print(f"Файл {filename} не знайдено.")

def search_student(name):
    if not os.path.exists(FILENAME):
        print("Файл не знайдено!")
        return
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            student, score = line.strip().split(";")
            if name.lower() in student.lower():
                print(f"Знайдено: {student}, бал = {score}")
                return
    print("Студента не знайдено!")

def sort_by_score():
    if not os.path.exists(FILENAME):
        print("Файл не знайдено!")
        return
    with open(FILENAME, "r", encoding="utf-8") as f:
        students = []
        for line in f:
            name, score = line.strip().split(";")
            students.append((name, int(score)))

    students.sort(key=lambda x: x[1], reverse=True)

    with open("sorted_" + FILENAME, "w", encoding="utf-8") as f:
        for name, score in students:
            f.write(f"{name};{score}\n")

    print("Файл відсортовано і збережено як sorted_students.txt")

if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()
    search_file("students.txt")
    search_student("Марія")
    sort_by_score()
    read_file()
