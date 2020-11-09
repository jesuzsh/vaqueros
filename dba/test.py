from database import Database

if __name__ == "__main__":
  db = Database()
  
  fake_expenditure = None

  db.write.expenditure(fake_expenditure)
