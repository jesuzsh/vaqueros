module v/cards

go 1.15

replace v/database => ../database

require (
	github.com/mattn/go-sqlite3 v1.14.5 // indirect
	gorm.io/driver/sqlite v1.1.3 // indirect
	gorm.io/gorm v1.20.7
)
