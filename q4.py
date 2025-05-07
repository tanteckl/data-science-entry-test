def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return
    
    return s[::-1]  # Slicing technique to reverse the string


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
print(string_reverse("Hello World"))  # Expected output: "dlroW olleH"
print(string_reverse("Python"))  # Expected output: "nohtyP"
