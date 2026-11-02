def TwoSum(nums:list[int],k:int):
    for cur in range(nums):
        for nxt in range(nums):
            if nums[cur]+nums[nxt] == k :
                return True
    else:
        return False



def TwoSum1(nums:list[int],k:int):
    seens = {}

    for idx,i in enumerate(nums):
        cmpl = k-i 
        if cmpl in seens.keys():
            return seens.get(cmpl), i
        seens[i]=idx
