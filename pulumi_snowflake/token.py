class Token:
    def __init__(self, sql):
        self.sql = sql

def token_equal(self, other):
    if isinstance(other, Token):
        return other.sql == self.sql
    return False

Token.__eq__ = token_equal
