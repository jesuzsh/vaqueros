package main

import (
	"fmt"
	"log"

	"vaqueros.io/greetings"
)

func main() {
	log.SetPrefix("greetings: ")
	log.SetFlags(0)

	names := []string{"J", "L", "M"}

	message, err := greetings.Hellos(names)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(message)
}
