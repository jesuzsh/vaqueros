package cards

import (
	//"errors"
	"fmt"

	"gorm.io/gorm"
)

type Card struct {
	gorm.Model
	Name  string
	Owner string
}

func (cd Card) Describe() {
	fmt.Printf("The %v card belongs to %v. ID: %v", cd.Name, cd.Owner, cd.ID)
}
