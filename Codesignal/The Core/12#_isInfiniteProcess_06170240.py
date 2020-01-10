# code 3 to 7 are unnecessary
def isInfiniteProcess(a, b):
    if a == b:
        return False
    elif a >= b:
        return True
    else:
        while (b-a) % 2 == 0:
            if (b-a) ==1:
                return True
            else:
                return False
        return True
