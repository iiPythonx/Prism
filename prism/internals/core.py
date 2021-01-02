# Modules
from .database import PrismDB

# Internal class
class Internals(object):

    def __init__(self):
        self.database = PrismDB()
