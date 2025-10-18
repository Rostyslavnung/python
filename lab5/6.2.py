import functions as f
def main():
    lst = [5, 3, 7, 2, 5, 0, 3, 8, 1]

    print("Original list:", lst)
    print("Sorted list:", f.sort_list(lst))
    print("Find 7:", f.find(7, lst))
    print("Find sequence [2, 5, 0]:", f.find_sequence_in_list(lst, [2, 5, 0]))
    print("First five minimal:", f.first_five_minimal(lst))
    print("First five maximal:", f.first_five_maximal(lst))
    print("Average value:", f.average_value(lst))
    print("List without duplicates:", f.list_without_duplicates(lst))


if __name__ == "__main__":
    main()