package costs

import (
	"fmt"
	"gorm.io/gorm"
)

type Cost struct {
	gorm.Model
	CardID       int
	CategoryName string
	Name         string
	Date         string
	Amount       int
}

func (cst Cost) Describe() {
	fmt.Printf("A purchase of %v was made at %v on %v", cst.Amount, cst.Name, cst.Date)
}
