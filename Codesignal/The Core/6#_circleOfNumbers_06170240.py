def circleOfNumbers(n, firstNumber):
    if firstNumber >= (n // 2):
        return firstNumber - ( n // 2 )
    else:
        return firstNumber + ( n // 2 )
