package patterns

import "fmt"

func ZigZag(n int) {
	for i := 0; i < 3; i++ { // height of zig-zag
		for j := 0; j < n; j++ {
			if i == 0 && (j%4 == 0 || j%4 == 1 || j%4 == 2) {
				fmt.Print("*")
			} else if i == 1 && (j%4 == 1 || j%4 == 3) {
				fmt.Print("*")
			} else if i == 2 && (j%4 == 2) {
				fmt.Print("*")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println()
	}
}
