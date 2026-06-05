package bit

func ElementAppersTwiceExceptOne(n []int) int {
	length := len(n)
	for i := 0; i < length; i++ {
		count := 1
		for j := 0; j < length; j++ {
			if (n[i] == n[j]) && (i != j) {
				count += 1
			}
		}
		if count == 1 {
			return n[i]
		}
	}
	return -1
}

func ElementAppersTwiceExceptOneV1(n []int) int {
	hashmap := make(map[int]int, 0)
	for _, value := range n {
		if count, ok := hashmap[value]; ok {
			hashmap[value] = count + 1
		}
		hashmap[value] = 1

	}
	for key, val := range hashmap {
		if val == 1 {
			return key
		}
	}
	return -1
}

func ElementAppersTwiceExceptOneV2(n []int) int {
	value := 0
	for _, element := range n {
		value ^= element
	}
	if value > 0 {
		return value
	}
	return -1
}

func ElementAppersTwiceExceptOneV3(n []int) int {
	// Loop from most significant bit and if count is even then make set bit in our answer
	// 1. Iterate over every bit
	// 2. Count no. of set bits in all nos.
	// if count is even then ans bit is set
	// else ans bit is not-set

	ans := 0
	length := len(n)

	for i := 0; i < 32; i++ {
		count := 0

		for j := 0; j < length; j++ {
			if CheckKthBitSet(n[j], i) {
				// bit is set then count
				count += 1
			}
		}

		if (count & 1) == 1 {
			// check bit is even
			ans = ans | (1 << i) // make bit as set bit
		}
	}
	if ans == 0 {
		return -1
	}
	return ans
}
