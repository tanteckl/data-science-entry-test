def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        return
    
    return [replace_val if item == find_val else item for item in lst]


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
my_list = [1, 2, 3, 2, 4]
modified_list = find_and_replace(my_list, 2, 9)
print(modified_list)  # Output: [1, 9, 3, 9, 4]

# - ["apple", "banana", "apple"], "apple", "orange"
my_list = ["apple", "banana", "apple"]
modified_list = find_and_replace(my_list, "apple", "orange")
print(modified_list)  # Output: ["orange", "banana", "orange"]
