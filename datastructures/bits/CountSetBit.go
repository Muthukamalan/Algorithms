package bits

func CountSetBit(n int) int {
	counter := 0
	for n > 0 {
		counter += n & 1
		n = n >> 1
	}
	return counter
}

func CountSetBitV1(n int) (counter int) {
	for n > 0 {
		n = n & (n - 1) // clear 1st, 2nd set bit
		counter++

	}
	return
}
