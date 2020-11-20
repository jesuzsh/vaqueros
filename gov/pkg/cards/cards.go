package cards

import (
	"errors"
	"fmt"

	"gorm.io/gorm"
	"v/database"
)

type Card struct {
	gorm.Model
	Name  string
	Owner string
}

func (cd Card) Describe() string {
	descr := fmt.Sprintf("The %v card belongs to %v.", cd.Name, cd.Owner)
	return descr
}

func (cd *Card) populateID() {
	db := database.MakeConnection()
	fmt.Println(db)
	//new_id := db.GenerateCardID()
	fmt.Println("Populating card ID.")
}

func NewCard(name string, owner string) (*Card, error) {
	if name == "" || owner == "" {
		return nil, errors.New("Missing a required field.")
	}
	cd := new(Card)
	cd.populateID()

	return cd, nil
}
