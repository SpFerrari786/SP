"""
Unit tests for math_utils module
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from math_utils import factorial, is_prime, fibonacci


class TestFactorial:
    """Test cases for factorial function"""
    
    def test_zero(self):
        assert factorial(0) == 1
    
    def test_one(self):
        assert factorial(1) == 1
    
    def test_positive_number(self):
        assert factorial(5) == 120
    
    def test_larger_number(self):
        assert factorial(10) == 3628800
    
    def test_negative_number(self):
        with pytest.raises(ValueError):
            factorial(-1)
    
    def test_non_integer(self):
        with pytest.raises(TypeError):
            factorial(5.5)
    
    def test_string_input(self):
        with pytest.raises(TypeError):
            factorial("5")


class TestIsPrime:
    """Test cases for is_prime function"""
    
    def test_prime_numbers(self):
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(13) is True
    
    def test_not_prime(self):
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False
    
    def test_zero_and_one(self):
        assert is_prime(0) is False
        assert is_prime(1) is False
    
    def test_negative_numbers(self):
        assert is_prime(-5) is False
    
    def test_large_prime(self):
        assert is_prime(97) is True
    
    def test_non_integer(self):
        with pytest.raises(TypeError):
            is_prime(5.5)


class TestFibonacci:
    """Test cases for fibonacci function"""
    
    def test_zero(self):
        assert fibonacci(0) == []
    
    def test_one(self):
        assert fibonacci(1) == [0]
    
    def test_two(self):
        assert fibonacci(2) == [0, 1]
    
    def test_five(self):
        assert fibonacci(5) == [0, 1, 1, 2, 3]
    
    def test_ten(self):
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    def test_negative_number(self):
        with pytest.raises(ValueError):
            fibonacci(-1)
    
    def test_non_integer(self):
        with pytest.raises(TypeError):
            fibonacci(5.5)
    
    def test_sequence_property(self):
        """Test that each number is the sum of previous two"""
        result = fibonacci(8)
        for i in range(2, len(result)):
            assert result[i] == result[i-1] + result[i-2]
