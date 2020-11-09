from read import Read
from write import Write

class Database:
  """
  Master database class. Parent class of CRUD modules.
  """
  def __init__(self):
    self.read = Read()
    self.write = Write()
