def sumSquares(k):
    sum = 0
    for i in range(k+1):
        sum = sum + i**2
    return sum


def squareSum(k):
    sum = 0
    for i in range(k+1):
        sum = sum + i
    sum = sum**2

    return sum

squareSum(100)-sumSquares(100)

