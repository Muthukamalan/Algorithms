package patterns

func HollowNumericPyramid(n int) {
	for i := 1; i <= n; i++ {
		for j := 1; j <= i-1; j++ {
			print("_")
		}
		print(i)
		for k := 1; k <= 2*(n-i)-1; k++ {
			print("_")
		}
		if i != n {
			print(i)
		}
		for j := 1; j <= i-1; j++ {
			print("_")
		}
		println()
	}
}
