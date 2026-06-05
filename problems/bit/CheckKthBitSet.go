package bit

func CheckKthBitSet(n int, i int) bool {
	// n=20 and i=3

	switch (n >> i) & 1 {
	case 1:
		// the bit is set
		return true
	default:
		// the bit is 0
		return false
	}
}
