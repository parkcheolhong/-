#!/usr/bin/env python3
"""
Example code for testing the code analysis functionality
이 파일은 코드 분석 기능을 테스트하기 위한 예제 코드입니다.
"""

def fibonacci(n):
    """Calculate fibonacci number (with potential issues for analysis)"""
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # This is inefficient - recursive without memoization
    return fibonacci(n-1) + fibonacci(n-2)

def divide_numbers(a, b):
    """Divide two numbers (potential division by zero)"""
    return a / b  # No error handling

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add_item(self, item):
        # No input validation
        self.data.append(item)
    
    def get_average(self):
        # Potential division by zero
        return sum(self.data) / len(self.data)

# Global variable usage (not recommended)
global_counter = 0

def increment_counter():
    global global_counter
    global_counter += 1
    return global_counter

if __name__ == "__main__":
    # Test the functions
    print(f"Fibonacci of 10: {fibonacci(10)}")
    print(f"Division result: {divide_numbers(10, 2)}")
    
    processor = DataProcessor()
    processor.add_item(5)
    processor.add_item(10)
    print(f"Average: {processor.get_average()}")
    
    print(f"Counter: {increment_counter()}")