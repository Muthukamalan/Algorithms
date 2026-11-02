def CallPatternOne(n:int)->None:
    for row in range(n):
        print("#",end="")
        for col in range(n-1):
            print("_",end="")
        print("#\n")