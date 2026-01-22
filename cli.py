#!/usr/bin/env python3
"""
CLI tool for SP utilities

This provides a command-line interface to the SP utility functions.
"""

import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from string_utils import reverse_string, is_palindrome, count_vowels, capitalize_words
from math_utils import factorial, is_prime, fibonacci


def print_help():
    """Print help message"""
    help_text = """
SP Utilities CLI
================

Usage: python cli.py <command> [arguments]

String Commands:
    reverse <text>          - Reverse a string
    palindrome <text>       - Check if text is a palindrome
    vowels <text>          - Count vowels in text
    capitalize <text>      - Capitalize each word in text

Math Commands:
    factorial <n>          - Calculate factorial of n
    prime <n>              - Check if n is prime
    fibonacci <n>          - Generate first n Fibonacci numbers

Examples:
    python cli.py reverse "hello world"
    python cli.py palindrome "racecar"
    python cli.py factorial 5
    python cli.py fibonacci 10

Use 'python cli.py help' to show this message.
    """
    print(help_text)


def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2 or sys.argv[1] == "help":
        print_help()
        return
    
    command = sys.argv[1].lower()
    
    try:
        # String commands
        if command == "reverse":
            if len(sys.argv) < 3:
                print("Error: Please provide a string to reverse")
                return
            text = " ".join(sys.argv[2:])
            print(reverse_string(text))
        
        elif command == "palindrome":
            if len(sys.argv) < 3:
                print("Error: Please provide a string to check")
                return
            text = " ".join(sys.argv[2:])
            result = is_palindrome(text)
            print(f"'{text}' is {'a palindrome' if result else 'not a palindrome'}")
        
        elif command == "vowels":
            if len(sys.argv) < 3:
                print("Error: Please provide a string to analyze")
                return
            text = " ".join(sys.argv[2:])
            count = count_vowels(text)
            print(f"Number of vowels: {count}")
        
        elif command == "capitalize":
            if len(sys.argv) < 3:
                print("Error: Please provide a string to capitalize")
                return
            text = " ".join(sys.argv[2:])
            print(capitalize_words(text))
        
        # Math commands
        elif command == "factorial":
            if len(sys.argv) < 3:
                print("Error: Please provide a number")
                return
            try:
                n = int(sys.argv[2])
            except ValueError:
                print("Error: Please provide a valid integer")
                return
            result = factorial(n)
            print(f"factorial({n}) = {result}")
        
        elif command == "prime":
            if len(sys.argv) < 3:
                print("Error: Please provide a number")
                return
            try:
                n = int(sys.argv[2])
            except ValueError:
                print("Error: Please provide a valid integer")
                return
            result = is_prime(n)
            print(f"{n} is {'prime' if result else 'not prime'}")
        
        elif command == "fibonacci":
            if len(sys.argv) < 3:
                print("Error: Please provide a number")
                return
            try:
                n = int(sys.argv[2])
            except ValueError:
                print("Error: Please provide a valid integer")
                return
            result = fibonacci(n)
            print(f"First {n} Fibonacci numbers: {result}")
        
        else:
            print(f"Error: Unknown command '{command}'")
            print("Use 'python cli.py help' for usage information")
    
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
