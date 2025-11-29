# Easy algorithmic tasks on HackerRank in a single file
# No need for such big pre-existing code for these tasks. HackerRank is weird

# Warmup
# 1. Solve Me First
"""
def solveMeFirst(a,b):
	return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
"""

# 2. Simple Array Sum
"""
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
"""

# 3. Compare the Triplets
"""
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
"""

# 4. A Very Big Sum
"""
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
"""

# 5. Diagonal Difference
"""
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
"""

# 6. Plus Minus
"""
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
"""

# 7. Staircase
"""
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
"""

# 8. Min-Max Sum
"""
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minimum, maximum, arr_sum = arr[0], arr[0], arr[0]
    for i in range(1, len(arr)):
        arr_sum += arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] > maximum:
            maximum = arr[i]
    
    print(arr_sum-maximum, arr_sum-minimum)
"""

# 9. Birthday Cake Candles
"""
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    tallest = candles[0]
    heights = {tallest: 1}
    for i in range(1, len(candles)):
        if candles[i] > tallest:
            tallest = candles[i]
        heights[candles[i]] = heights.get(candles[i], 0) + 1
    
    return heights[tallest]
"""

# 10. Time Conversion
"""
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] == 'PM':
        if s[:2] == '12':
            return s[:-2]
        return str(int(s[:2])+12) + s[2:-2]
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:-2]

    return s[:-2]
"""

# Implementation
# 11. Grading Students
"""
#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] > 37 and grades[i] % 5 != 0:
            tmp = 5 - grades[i] % 10
            if tmp < 0:
                tmp += 5
            tmp += grades[i]
            if tmp - grades[i] < 3:
                grades[i] = tmp
    return grades
"""

# 12. Apple and Orange
"""
#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    n = max(len(apples), len(oranges))
    m = True if len(apples) >= len(oranges) else False
    ad, od = 0, 0
    for i in range(n):
        if m:
            if i < len(oranges):
                if s <= oranges[i] + b <= t:
                    od += 1
            if s <= apples[i] + a <= t:
                ad += 1
        else:
            if i < len(apples):
                if s <= apples[i] + a <= t:
                    ad += 1
            if s <= oranges[i] + b <= t:
                od += 1
    print(ad)
    print(od)
"""

# 13. Number Line Jumps
"""
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    return 'YES' if (v1 > v2 and ((x2 - x1) % (v1 - v2)) == 0) or (x1 == x2) else 'NO'
"""

# 14. Between Two Sets
"""
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    nums = set()
    for v in range(a[-1], b[0]+1, a[-1]):
        print(v)
        ca, cb = True, True
        for va in a:
            if not (v % va == 0):
                ca = False
                break
        for vb in b:
            if not (vb % v == 0):
                cb = False
                break
        if ca and cb:
            nums.add(v)

    return len(nums)
"""
