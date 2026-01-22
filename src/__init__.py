"""
SP - Skills Practice Package

A collection of utility functions for enhancing coding skills.
"""

__version__ = "0.1.0"

from .string_utils import reverse_string, is_palindrome, count_vowels, capitalize_words
from .math_utils import factorial, is_prime, fibonacci

__all__ = [
    "reverse_string",
    "is_palindrome", 
    "count_vowels",
    "capitalize_words",
    "factorial",
    "is_prime",
    "fibonacci",
]
