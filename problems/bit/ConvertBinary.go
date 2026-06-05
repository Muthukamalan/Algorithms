package bit

import "strconv"

func ConvertBinary(n int) string {
	return strconv.FormatInt((int64(n)), 2)
}

func ConvertBinaryV1(n int) string {
	if n == 0 {
		return "0"
	}
	binary := ""
	for n > 0 {
		r := n % 2
		binary = strconv.Itoa(r) + binary
		n /= 2
	}
	return binary
}

func ConvertBinaryV2(n int) string {
	buf := make([]byte, 32)

	for i := 31; i >= 0; i-- {
		// '0' is ASCII 48.
		// Adding n&1 results in "0"/"48" or "1"
		buf[i] = '0' + byte(n&1)
		n = n >> 1
	}

	return string(buf)
}
