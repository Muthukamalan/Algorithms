package patterns

import "fmt"

func RightJustifiedLeftTriangle(n int) {
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			fmt.Print("_")
		}
		for j := 0; j < n-i; j++ {
			fmt.Print("#")
		}
		fmt.Println()
	}
}
