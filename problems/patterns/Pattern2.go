package patterns

import "fmt"

func LeftJustifiedRightTriangle(n int) {
	for i := 1; i <= n; i++ {
		// Print #
		for j := 0; j < i; j++ {
			fmt.Print("#")
		}

		// Print -
		for j := i; j < n; j++ {
			fmt.Print("-")
		}

		fmt.Println()
	}
}
