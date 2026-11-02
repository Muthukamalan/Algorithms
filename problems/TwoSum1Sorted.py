def TwoSum1Sorted(numbers: list[int], target: int) -> list[int]:
    start = 0 
    end = len(numbers) - 1 

    while start < end:
        current_sum = numbers[start] + numbers[end]
        if current_sum == target:
            return [start, end]  # Using a list for consistency
        elif current_sum < target:
            start += 1
        else:  # Replaced elif with else since it's the only remaining condition
            end -= 1
            
    return [-1, -1]