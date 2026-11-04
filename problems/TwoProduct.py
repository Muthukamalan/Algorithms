# Pair Product

def PairProduct(numbers:list[int],target:int):
    if len(numbers)<2:
        raise ValueError("Not valid list!")
    for idx1, i in enumerate(numbers):
        for idx2,j in enumerate(numbers):
            if idx1<idx2 and i*j==target:
                return (idx1,idx2)
    return (-1,-1)

def PairProduct1(numbers: list[int], target: int) -> bool:
    seen = dict()

    for idx,num in enumerate(numbers):
        
        if num!=0 and target%num==0:
            compl = target/num 
            if compl in seen:
                return ( seen.get(compl),idx )

        elif  num==0 and target==0:
            if 0 in seen:
                return (seen[0],idx)
        
        seen[num]=idx 