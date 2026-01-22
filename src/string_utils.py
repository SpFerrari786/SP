"""
String Utilities Module

This module provides various string manipulation utilities
to demonstrate good Python coding practices.
"""


def reverse_string(text: str) -> str:
    """
    Reverse a given string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove spaces and convert to lowercase for comparison
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a string.
    
    Args:
        text (str): The string to analyze
        
    Returns:
        int: The number of vowels in the string
        
    Example:
        >>> count_vowels("hello world")
        3
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Note: This function normalizes whitespace, converting multiple spaces
    between words into single spaces.
    
    Args:
        text (str): The string to capitalize
        
    Returns:
        str: The string with each word capitalized
        
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("hello  world")
        'Hello World'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return " ".join(word.capitalize() for word in text.split())
