"""
Unit tests for string_utils module
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from string_utils import reverse_string, is_palindrome, count_vowels, capitalize_words


class TestReverseString:
    """Test cases for reverse_string function"""
    
    def test_simple_string(self):
        assert reverse_string("hello") == "olleh"
    
    def test_empty_string(self):
        assert reverse_string("") == ""
    
    def test_single_character(self):
        assert reverse_string("a") == "a"
    
    def test_palindrome(self):
        assert reverse_string("racecar") == "racecar"
    
    def test_with_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            reverse_string(123)


class TestIsPalindrome:
    """Test cases for is_palindrome function"""
    
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True
    
    def test_not_palindrome(self):
        assert is_palindrome("hello") is False
    
    def test_palindrome_with_spaces(self):
        assert is_palindrome("race car") is True
    
    def test_case_insensitive(self):
        assert is_palindrome("RaceCar") is True
    
    def test_empty_string(self):
        assert is_palindrome("") is True
    
    def test_single_character(self):
        assert is_palindrome("a") is True
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            is_palindrome(123)


class TestCountVowels:
    """Test cases for count_vowels function"""
    
    def test_simple_string(self):
        assert count_vowels("hello") == 2
    
    def test_no_vowels(self):
        assert count_vowels("xyz") == 0
    
    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5
    
    def test_uppercase_vowels(self):
        assert count_vowels("AEIOU") == 5
    
    def test_mixed_case(self):
        assert count_vowels("Hello World") == 3
    
    def test_empty_string(self):
        assert count_vowels("") == 0
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            count_vowels(123)


class TestCapitalizeWords:
    """Test cases for capitalize_words function"""
    
    def test_simple_sentence(self):
        assert capitalize_words("hello world") == "Hello World"
    
    def test_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"
    
    def test_all_uppercase(self):
        assert capitalize_words("HELLO WORLD") == "Hello World"
    
    def test_single_word(self):
        assert capitalize_words("hello") == "Hello"
    
    def test_empty_string(self):
        assert capitalize_words("") == ""
    
    def test_multiple_spaces(self):
        result = capitalize_words("hello  world")
        assert "Hello" in result and "World" in result
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            capitalize_words(123)
