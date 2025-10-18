def find_key(d, key):
    return d.get(key, "Key not found")

def find_value(lst, value):
    return lst.index(value) if value in lst else "Value not found"

def find_sequence_in_list(lst, subseq):
    for i in range(len(lst) - len(subseq) + 1):
        if lst[i:i+len(subseq)] == subseq:
            return i
    return "Sequence not found"

def first_five_minimal(lst):
    return sorted(lst)[:5]

def first_five_maximal(lst):
    return sorted(lst, reverse=True)[:5]

def average_value(lst):
    return sum(lst) / len(lst) if lst else 0

def find_zero_values(lst):
    return [i for i, v in enumerate(lst) if v == 0]

def list_without_duplicates(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

def find_sequence_in_string(s, subseq):
    idx = s.find(subseq)
    return idx if idx != -1 else "Sequence not found"

def split_sentence(sentence):
    return sentence.split()

dictionary = {'a': 1, 'b': 2, 'c': 3}
lst = [1, 0, 3, 5, 0, 2, 7, 5, 3, 0]
sentence = "lorem ipsum dolor sit amet,   consectetur  adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


while True:
    print("\n=== MENU ===")
    print("1. Search in dictionary by key")
    print("2. Search element by value in list")
    print("3. Search sequence of elements in list")
    print("4. First 5 minimal elements in list")
    print("5. First 5 maximal elements in list")
    print("6. Average value in list")
    print("7. All zero elements in list (indices)")
    print("8. List without duplicates")
    print("9. Search sequence in string")
    print("10. Split sentence into words")
    print("0. Exit")

    choice = input("Your choice: ")

    if choice == "0":
        break
    elif choice == "1":
        key = input("Enter key: ")
        print("Result:", find_key(dictionary, key))
    elif choice == "2":
        value = int(input("Enter value: "))
        print("Result:", find_value(lst, value))
    elif choice == "3":
        subseq = list(map(int, input("Enter sequence (space separated): ").split()))
        print("Result:", find_sequence_in_list(lst, subseq))
    elif choice == "4":
        print("Result:", first_five_minimal(lst))
    elif choice == "5":
        print("Result:", first_five_maximal(lst))
    elif choice == "6":
        print("Result:", average_value(lst))
    elif choice == "7":
        print("Result (indices of zeros):", find_zero_values(lst))
    elif choice == "8":
        print("Result:", list_without_duplicates(lst))
    elif choice == "9":
        subseq = input("Enter substring: ")
        print("Result:", find_sequence_in_string(sentence, subseq))
    elif choice == "10":
        print("Result:", split_sentence(sentence))
    else:
        print("Invalid choice, try again.")