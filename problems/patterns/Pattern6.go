package patterns

import "fmt"

func PyramidPattern(n int) {
	for i := 1; i <= n; i++ {
		for j := 0; j < n-i+1; j++ {
			fmt.Print("#")
		}

		for j := 0; j < 2*(i-1); j++ {
			fmt.Print("_")
		}

		for j := 0; j < n-i+1; j++ {
			fmt.Print("#")
		}

		fmt.Println()
	}
}
