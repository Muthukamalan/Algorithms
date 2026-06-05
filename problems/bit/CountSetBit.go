package bit

func CountSetBit(n int) int {
	set_bit := 0
	for n > 0 {
		if (n & 1) == 1 {
			set_bit += 1
		}
		n = n >> 1
	}
	return set_bit
}

func CountSetBitV1(n int) int {
	set_bit := 0
	for i := 0; i < 32; i++ {
		if CheckKthBitSet(n, i) {
			set_bit += 1
		}

	}
	return set_bit
}
