package patterns

import "fmt"

func RightJustifiedRightTriangle(n int) {
	for i := 1; i < n-1; i++ {
		for i := i; i < n; i++ {
			fmt.Printf("_")
		}
		for i := n - i; i < n; i++ {
			fmt.Printf("#")
		}
		fmt.Println()
	}
}
