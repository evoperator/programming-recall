# HackerRank's Software Engineer Prep Kit
# Practice challenges

# Arrays and Basic Problem Solving
# Count Elements Greater Than Previous Average
"""#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) > 0:
        average = [responseTimes[0]]
    count = 0
    for i in range(1, len(responseTimes)):
        if responseTimes[i] > sum(average)/len(average):
            count += 1
        average.append(responseTimes[i])

    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
"""

# Strings and Pattern Matching
"""#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    string = []
    for c in code:
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
            string.append(c.lower())
        
    return 1 if ''.join(string) == ''.join(string[::-1]) else 0

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
"""

