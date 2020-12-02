package migrations

import (
	db "v/database"
)

// Migrate performs any creations and changes to the database.
func Migrate() {
	db.Migrate()
}
