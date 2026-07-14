package patterns

import "fmt"

func InversePyramidPattern(n int) {
	for i := n; i >= 1; i-- {
		// Print left #
		for j := 0; j < n-i+1; j++ {
			fmt.Print("#")
		}

		// Print _
		for j := 0; j < 2*(i-1); j++ {
			fmt.Print("_")
		}

		// Print right #
		for j := 0; j < n-i+1; j++ {
			fmt.Print("#")
		}

		fmt.Println()
	}
}
