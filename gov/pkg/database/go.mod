module v.com/database

go 1.13

replace v.com/cards => ../../pkg/cards

replace v.com/costs => ../../pkg/costs

require (
	gorm.io/driver/sqlite v1.1.4
	gorm.io/gorm v1.20.8
	v.com/cards v0.0.0-00010101000000-000000000000
	v.com/costs v0.0.0-00010101000000-000000000000
)
