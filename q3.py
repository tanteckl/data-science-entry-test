def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    dct[key] = value
    return dct


# Task 2 - Invoking the function with given scenarios
# - {}, "name", "Alice"
print(update_dictionary({}, "name", "Alice"))  # Expected output: {'name': 'Alice'}
# - {"age": 25}, "age", 26
print(update_dictionary({"age": 25}, "age", 26))  # Expected output + print: Original value for 'age': 25, {'age': 26}