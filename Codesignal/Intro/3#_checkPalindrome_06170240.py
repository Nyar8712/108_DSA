def checkPalindrome(inputString):
    a = reversed(list(inputString))
    if list(a) == list(inputString):
        return True
    else:
        return False
