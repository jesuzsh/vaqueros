package main

import (
	"fmt"

	"v/cards"
)

func main() {
	fmt.Println("Welcome to your budget.")
	//cd := cards.Card{Name: "Chime", Owner: "Jesus"}
	//cd.Save()
	cards.List()
	//fmt.Println(cd.Describe())
}
