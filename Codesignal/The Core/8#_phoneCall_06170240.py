def phoneCall(min1, min2_10, min11, s):
        if s == 0:
            return 0    
        elif s <= 10:
            return 1 + (s - min1) // min2_10
        else:
            return 10 + ( s - min1 - (min2_10*9)) // min11
