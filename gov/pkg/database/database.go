package database

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"v/cards"
)

func open() *gorm.DB {
	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	return db
}

func Migrate() {
	db := open()
	db.AutoMigrate(&Card{})
}

func SaveCard() {
	db := open()
	db.Create(cd)
}
