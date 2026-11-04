# 2342. Max Sum of a Pair With Equal Sum of Digits
def sum_of_digits(number:int)->int:
    sum = 0
    while number>0:
        digit = number%10
        number //= 10
        sum+=digit
    return sum 
    

def MaximumSum(nums:list[int])->int:
    seens:dict[int,int] = {}
    result  = -1 

    for idx,num in enumerate(nums):
        digits_sum = sum_of_digits(num)

        if digits_sum in seens:
            current_sum =  num + seens.get(digits_sum)

            result = max(result, current_sum)

            # keep the maximum individual umber
            seens[digits_sum] = max(seens.get(digits_sum), num)
        else:
            seens[digits_sum] = num
    return -1