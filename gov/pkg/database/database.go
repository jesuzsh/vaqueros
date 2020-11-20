package database

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func MakeConnection() *gorm.DB {
	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})

	if err != nil {
		panic("failed to connect database")
	}

	//db.AutoMigrate(&cards.Card{})

	return db
}
