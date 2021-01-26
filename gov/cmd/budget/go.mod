module budget

go 1.15

replace v.com/cards => ../../pkg/cards

replace v.com/database => ../../pkg/database

require (
	v.com/cards v0.0.0-00010101000000-000000000000 // indirect
	v.com/database v0.0.0-00010101000000-000000000000
)
