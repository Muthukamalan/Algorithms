package bit

import "fmt"

func BitMaskingExample(N int) {
	for v := range 1 << N {
		fmt.Printf("Binary: %04b ;; value:: %v\n", v, v)
	}
}
