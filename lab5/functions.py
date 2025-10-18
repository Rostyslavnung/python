"""
Module list_utils
Contains utility functions for working with lists.
"""

def sort_list(lst):
    """
    Sort a list in ascending order.

    Args:
        lst (list): List of elements.

    Returns:
        list: Sorted list.
    """
    return sorted(lst)


def find(item, lst):
    """
    Check if an item exists in a list.

    Args:
        item: Element to find.
        lst (list): List to search in.

    Returns:
        bool: True if item is found, False otherwise.
    """
    return item in lst


def find_sequence_in_list(lst, subseq):
    """
    Find a subsequence in a list.

    Args:
        lst (list): Source list.
        subseq (list): Subsequence to find.

    Returns:
        int or str: Starting index of subsequence if found, 
                    otherwise "Sequence not found".
    """
    for i in range(len(lst) - len(subseq) + 1):
        if lst[i:i+len(subseq)] == subseq:
            return i
    return "Sequence not found"


def first_five_minimal(lst):
    """
    Get the first five minimal elements from the list.

    Args:
        lst (list): List of elements.

    Returns:
        list: List of five minimal elements (or fewer if list is shorter).
    """
    return sorted(lst)[:5]


def first_five_maximal(lst):
    """
    Get the first five maximal elements from the list.

    Args:
        lst (list): List of elements.

    Returns:
        list: List of five maximal elements (or fewer if list is shorter).
    """
    return sorted(lst, reverse=True)[:5]


def average_value(lst):
    """
    Calculate the average value of a list.

    Args:
        lst (list): List of numbers.

    Returns:
        float: Average value, or 0 if list is empty.
    """
    return sum(lst) / len(lst) if lst else 0


def list_without_duplicates(lst):
    """
    Remove duplicates from a list while preserving the first occurrence.

    Args:
        lst (list): List with possible duplicates.

    Returns:
        list: List without duplicates (order preserved).
    """
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result
