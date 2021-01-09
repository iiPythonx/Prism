# Modules
from .database import PrismDB
from Levenshtein.StringMatcher import StringMatcher

# Internal class
class Internals(object):

    def __init__(self):
        self.database = PrismDB()

    def locate_user(self, user):

        """
        Function that uses the Levenshtein string distance method to
        locate a user based on a fraction of their name, user ID, etc.

        This requires the SERVER MEMBERS intent to be enabled.
        """

        # Create the string matcher
        matcher = StringMatcher()
        matcher.set_seqs(1, 1)

        return user
