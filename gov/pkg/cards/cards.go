package cards

import (
	//"errors"
	"fmt"

	"gorm.io/gorm"
	"v/database"
	fo "v/finos"
)

// Card represents the financial object, Credit/Debit cards.
type Card struct {
	gorm.Model
	Name  string
	Owner string
}

// Save persists the Card instance. If fields are not of valid form, err will
// say why.
func (cd fo.Card) Save() {
	db.SaveCard(cd)
}

// Show obtains a card to report. Returns a report of type string.
func (cd fo.Card) List() {
	cards := database.getCards()

	for _, cd := range cards {
		descr := cd.describe()
		fmt.Println(descr)
	}
}

func (cd fo.Card) describe() string {
	Println("The %v card belongs to %v.", cd.Name, cd.Owner)
}

/*
func (cd *Card) populateID() {
	db := database.MakeConnection()

	db.Au
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
*/
