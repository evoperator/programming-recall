# Easy tasks in Python in a single file

# Introduction
# 1. Say "Hello, World!" With Python
"""print("Hello, World!")"""

# 2. Python If-Else
"""# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 0:
        if 2 <= n <= 5 or n > 20:
            print("Not Weird")
        else:
            print("Weird")
    else:
        print("Weird")"""

# 3. Arithmetic Operators
"""if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b, a-b, a*b, sep="\n")"""

# 4. Python: Division
"""if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b, a/b, sep="\n")"""

# 5. Loops
"""if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)"""

# 6. Write a function # Medium
"""def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))"""

# 7. Print Function
"""if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1, end="")"""

# Basic Data Types
# 8. List Comprehensions
"""if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])"""

# 9. Find the Runner-Up Score!
"""if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True)
    
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            break
        if arr[i] != arr[i+1]:
            i += 1
            break
            
    print(arr[i])"""

# 10. Nested Lists
"""if __name__ == '__main__':
    students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score)
        
    students.sort(key = lambda x: x[1])
    scores = list(scores)
    scores.sort(reverse=True)
    scores.pop()
    
    names = []
    for student in students:
        if student[1] == scores[-1]:
            names.append(student[0])
            
    names.sort()
    print('\n'.join(names))"""

# 11. Finding the percentage
"""if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    print(f"{(sum(student_marks[query_name])/len(student_marks[query_name])):.2f}")"""