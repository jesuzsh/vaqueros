package main

import (
	"fmt"

	"v/finos"
	"v/migrations"
)

type FinO interface {
	List()
}

func main() {
	migrations.Migrate()

	fmt.Println("Welcome to your budget.")

}
