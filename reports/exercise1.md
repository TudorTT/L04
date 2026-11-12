# Bug reports for exercise1.py

Line: 3  
Problem: The function `is_even(n)` returns `True` when `n % 2 == 1`, which is true for odd numbers, not even numbers.  
Example: return n % 2 == 1  
Fix: return n % 2 == 0

Line: 8  
Problem: The `rectangle_area(width, height)` function incorrectly returns `width + height`, which is the perimeter-related sum, not the area of a rectangle.  
Example: return width + height  
Fix: return width * height

Line: 13  
Problem: The `double(n)` function returns `n + 2`, which is not twice the number. Twice the number should be `n * 2` or `n + n`.  
Example: return n + 2  
Fix: return n * 2
