package main

import (
	"fmt"

	db "v.com/database"
)

func main() {
	fmt.Println("Welcome to your budget.")

	db.ListCards()
}
