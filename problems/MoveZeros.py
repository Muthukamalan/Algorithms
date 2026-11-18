def MoveZeros(nums:list[int])->list[int]:
    N = len(nums)

    if N<2:
        return nums

    nonZeroIndex = 0 

    for pos in range(0,N):
        if nums[pos]!=0:
            nums[nonZeroIndex]=nums[pos]
            nonZeroIndex+=1

    while nonZeroIndex<N:
        nums[nonZeroIndex]=0
        nonZeroIndex+=1

    return nums

