def inSequence(A, B, C):
    if C==0:
        if A==B:
            return 1
        else:
            return 0
    return 1 if ((B-A) % C == 0 and int((B-A)/C)>=0) else 0


print(inSequence(A=4,B=-12,C=4))