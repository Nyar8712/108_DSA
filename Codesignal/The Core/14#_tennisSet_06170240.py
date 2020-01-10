def tennisSet(score1, score2):
    if (score1 == 6 and score2<5) or (score1 == 7 and 5 <=score2<=6):
        return True
    elif (score1<5 and score2 == 6) or (score2 ==7 and 5<= score1 <=6):
        return True
    else:
        return False
