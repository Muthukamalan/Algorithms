package bits

func UnsetIBit(n, i int) int {
	return n &^ (1 << i)
}
