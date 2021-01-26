package database

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	cd "v.com/cards"
	ct "v.com/costs"
)

type FinObj interface {
	Describe()
}

type DBGateway struct {
	cnxn *gorm.Db)
}

func SaveCost(cst ct.Cost) {
	db := makeConnection()
	db.AutoMigrate(&cst)

	db.Create(&cst)
}

func ListCards() {
	db := makeConnection()

	var cards []cd.Card
	db.Find(&cards)

	for _, card := range cards {
		report(card)
	}
}

func ListCosts() {
	db := makeConnection()

	var costs []ct.Cost
	db.Find(&costs)

	for _, cost := range costs {
		report(cost)
	}
}

func report(fo FinObj) {
	fo.Describe()
}

func makeConnection() *gorm.DB {
	db, err := gorm.Open(sqlite.Open("racks.db"), &gorm.Config{})

	if err != nil {
		panic("failed to connect database")
	}

	return db
}
