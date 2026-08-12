package bits

func ToggleIBit(n, i int) int {
	return n ^ (1 << i)

}
