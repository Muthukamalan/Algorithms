package patterns

import "fmt"

func LeftJustifiedLeftTriangle(n int) {
	for i := n; i >= 1; i-- {
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
