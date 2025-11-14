# Easy algorithmic tasks on HackerRank in a single file
# No need for such big pre-existing code for these tasks. HackerRank is weird

# Warmup
# 1. Solve Me First
"""def solveMeFirst(a,b):
	return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)"""

# 2. Simple Array Sum
"""#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    arraySum = 0
    for e in ar:
        arraySum += e
    
    return arraySum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
"""

# 3. Compare the Triplets
"""#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    arr = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            arr[0] += 1
        if a[i] < b[i]:
            arr[1] += 1
        
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
"""

# 4. A Very Big Sum
"""#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    ar_sum = 0
    for e in ar:
        ar_sum += e
        
    return ar_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
"""

# 5. Diagonal Difference
"""#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    lrd = arr[0][0]
    for l in range(1, len(arr)):
        lrd += arr[l][l]
        
    rld = arr[0][-1]
    for r in range(len(arr)-1, 0, -1):
        rld += arr[len(arr)-r][r-1]
        
    return abs(lrd - rld)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
"""

# 6. Plus Minus
"""#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    larr = len(arr)
    p, n, z = 0, 0, 0
    
    for a in arr:
        if a > 0:
            p += 1
        if a < 0:
            n += 1
        if a == 0:
            z += 1
    
    print(f"{p/larr:.6f}")
    print(f"{n/larr:.6f}")
    print(f"{z/larr:.6f}")
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
"""

# 7. Staircase
"""#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    stairs = [' ']*n
    for i in range(n-1, -1, -1):
        stairs[i] = '#'
        print(''.join(stairs))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
"""
