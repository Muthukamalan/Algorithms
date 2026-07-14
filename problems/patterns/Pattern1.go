package patterns

import "fmt"

func CallPatternOne(n int) {
	for range n {
		fmt.Printf("#")
		for i := 0; i < n-1; i++ {
			fmt.Print("_")
		}
		fmt.Printf("#\n")

	}
}
