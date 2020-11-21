package database

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type FinObj interface {
	Save()
	List()
	Describe()
}

func Save(fo FinObj) {
	db := makeConnection()
	db.AutoMigrate(&fo)

	db.Create(&fo)
}

func List(fos FinObj) {
	db := makeConnection()
	db.Find(&fo)

	for _, fo := range fos {
		fmt.Println(fo.Describe())
	}
}

func makeConnection() *gorm.DB {
	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})

	if err != nil {
		panic("failed to connect database")
	}

	return db
}
