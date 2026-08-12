package bits

func CheckIBit(n, i int) bool {
	return (n>>i)&1 == 1
}

func CheckIBitV1(n, i int) (x bool) {
	x = n&(1<<i) > 0
	return
}
