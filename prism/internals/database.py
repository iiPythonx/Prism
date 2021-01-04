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

        # Clear database list
        self.dbs = {}

    def locate_db(self, db):

        """Returns the dictionary for the specified database"""
        return self.dbs[db]

    def insert_into(self, db_name, values):

        """Inserts "values" into the database "db_name" """

        # Locate database
        db = self.locate_db(db_name)

        # Perform inject
        value_key = "".join("?," for _ in range(len(values)))[:-1]
        db["cursor"].execute(f"INSERT INTO {db_name} VALUES ({value_key})", values)

        # Save database
        self.__savedb__()
        self.__opendb__()

    def remove_from(self, db_name, key, value):

        """Removes the database entry where key is set to value"""

        # Locate database
        db = self.locate_db(db_name)

        # Master execution
        db["cursor"].execute(f"DELETE FROM {db_name} WHERE {key}=?", (value,))

    def get_row_by_key(self, db_name, key, value):

        """Loops through the given database and returns the row containing key set to value."""

        # Locate database
        db = self.locate_db(db_name)

        # Loop through rows
        for row in db["cursor"].execute(f"SELECT * FROM {db_name} WHERE {key}=?", (value,)):
            return row

        # No record
        return None
