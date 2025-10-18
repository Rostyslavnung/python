import os

INPUT_FILE = "students.txt"     
OUTPUT_FILE_1 = "copy.txt"
OUTPUT_FILE_2 = "reverse.txt"

def copy_file():
    if not os.path.exists(INPUT_FILE):
        print("Вихідний файл не знайдено!")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines() 

    with open(OUTPUT_FILE_1, "w", encoding="utf-8") as f:
        f.writelines(lines)

    with open(OUTPUT_FILE_2, "w", encoding="utf-8") as f:
        f.writelines(reversed(lines))

    print("Файли успішно створені!")

if __name__ == "__main__":
    copy_file()
