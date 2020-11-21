package cards

import (
	//"errors"
	"fmt"

	"gorm.io/gorm"
	db "v/database"
)

type Card struct {
	gorm.Model
	Name  string
	Owner string
}

func (cd Card) Describe() string {
	descr := fmt.Sprintf("The %v card belongs to %v. ID: %v", cd.Name, cd.Owner, cd.ID)
	return descr
}

func (cd Card) Save() {
	db.Save(Card)
}

func List() {
	db.List([]Card{})
}
