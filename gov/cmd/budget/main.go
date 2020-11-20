package main

import (
	"fmt"

	"v/cards"
)

func main() {
	fmt.Println("Welcome to your budget.")
	cd := cards.Card{Name: "Amex", Owner: "Jesus"}
	fmt.Println(cd.Describe())
}
