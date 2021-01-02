# Modules
import sqlite3
from os import listdir

# Main database class
class PrismDB(object):

    """
    The database class that Prism uses for operations.
    """

    def __init__(self):
        self.dbs = {}
        self.__opendb__()

    def __opendb__(self):

        """Loads each database into memory for use with the bot"""

        # Loop through our database files
        for file in listdir("db"):

            # Check for a db file
            if file.endswith(".db"):

                # Connect to database
                conn = sqlite3.connect("db/" + file)
                cursor = conn.cursor()

                # Register database
                self.dbs[file[:-3]] = {
                    "conn": conn,
                    "cursor": cursor
                }

    def __savedb__(self):

        """Loops through each database and commits/closes it"""

        # Loop through our databases
        for db in self.dbs:

            # References
            db_ = self.dbs[db]

            # Commit changes
            db_["conn"].commit()

            # Close file
            db_["conn"].close()

            # Remove from database list
            del self.dbs[db]
