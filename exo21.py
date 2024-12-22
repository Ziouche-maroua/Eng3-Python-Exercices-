# Exercise: List Statistics

def length(lst):
    """
    Returns the number of elements in the list.

    Parameters:
        lst (list): The input list.

    Returns:
        int: The number of elements in the list.
    """
    return len(lst)

def mean(lst):
    """
    Calculates the arithmetic mean of the list.

    Parameters:
        lst (list): The input list containing numeric values.

    Returns:
        float: The arithmetic mean of the list, or None if the list is empty.
    """
    if not lst:
        return None
    return sum(lst) / len(lst)

def range_of_list(lst):
    """
    Returns the difference between the maximum and minimum values in the list.

    Parameters:
        lst (list): The input list containing numeric values.

    Returns:
        float: The range of the list, or None if the list is empty.
    """
    if not lst:
        return None
    return max(lst) - min(lst)

def median(lst):
    """
    Calculates the median of the list.

    Parameters:
        lst (list): The input list containing numeric values.

    Returns:
        float: The median of the list, or None if the list is empty.
    """
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2




def list_statistics(lst):
    """
    Creates a dictionary with statistics for the given list.

    Parameters:
        lst (list): The input list containing numeric values.

    Returns:
        dict: A dictionary containing length, mean, range, median, and standard deviation.
    """
    return {
        "Length": length(lst),
        "Mean": mean(lst),
        "Range": range_of_list(lst),
        "Median": median(lst),
       
    }

# Test cases
numbers = [1, 2, 3, 4, 5]
print("Test List:", numbers)
print("Length:", length(numbers))
print("Mean:", mean(numbers))
print("Range:", range_of_list(numbers))
print("Median:", median(numbers))
print("Statistics:", list_statistics(numbers))

# Edge cases
empty_list = []
print("\nEmpty List:", empty_list)
print("Statistics:", list_statistics(empty_list))

single_element_list = [42]
print("\nSingle Element List:", single_element_list)
print("Statistics:", list_statistics(single_element_list))

negative_numbers = [-5, -2, -3, -8, -1]
print("\nNegative Numbers List:", negative_numbers)
print("Statistics:", list_statistics(negative_numbers))

floating_point_numbers = [1.5, 2.3, 3.7, 4.2, 5.8]
print("\nFloating Point Numbers List:", floating_point_numbers)
print("Statistics:", list_statistics(floating_point_numbers))
