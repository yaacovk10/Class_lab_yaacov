def sumofdigits(num):
    """
    returns sum of digits of a number:
    """
    # Convert the number to a string to iterate through its digits
    str_number = str(num)
    
    # Initialize a variable to store the sum of digits
    digit_sum = 0
    
    # Iterate through each digit and add it to the sum
    for digit in str_number:
        digit_sum += int(digit)
    
    return digit_sum


def is_palindrome(num):
    """
    Returns True if the given number is a palindrome; otherwise, returns False
    """
    # Convert the number to a string for easy comparison
    str_number = str(num)
    
    # Reverse the string
    reversed_str = str_number[::-1]
    
    # Check if the original and reversed strings are the same
    return str_number == reversed_str