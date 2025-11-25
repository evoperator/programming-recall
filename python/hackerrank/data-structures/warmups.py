# "Easy" tasks about "data structures" on HackerRank in one file

# Arrays
# 1. Array - DS
"""
#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    return [a[i] for i in range(len(a)-1, -1, -1)]
"""

# 2. 2D Array - DS
"""
#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_sum = arr[1][1] + arr[0][0] + arr[0][1] + arr[0][2] + arr[2][0] + arr[2][1] + arr[2][2]
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr)-1):
            hourglass = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if hourglass > max_sum:
                max_sum = hourglass
    return max_sum
"""

# 3. Dynamic Array
"""
#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    ans = []
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    for q in queries:
        i, x, y = q
        idx = (x ^ lastAnswer) % n
        if i == 1:
            arr[(idx)].append(y)
        if i == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            ans.append(lastAnswer)
    return ans
"""

# 4. Left Rotation
"""
#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    d = d % len(arr)
    h = arr[:d]
    del arr[:d]
    arr.extend(h)
    return arr
"""
