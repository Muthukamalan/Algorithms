package main

import (
	"fmt"

	"muthu.dsa/problems/bit"
)

func main() {
	fmt.Printf("Convert number into binary %s\n", bit.ConvertBinaryV2(20))
	fmt.Printf("Is the bit set? %v\n", bit.CheckKthBitSet(20, 3))
	fmt.Printf("Number of set Bits %v\n", bit.CountSetBit(20))
	fmt.Printf("Number of set Bits %v\n", bit.CountSetBitV1(20))
	fmt.Printf("Check Element Appears Twice %v\n", bit.ElementAppersTwiceExceptOneV3([]int{1, 3, 6, 5, 3, 1, 5, 6, 9, 718, 9, 100, 718}))
}
