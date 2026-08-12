package bits

func ToggleFirstIBit(n int) int {
	return n & (n - 1)
}
