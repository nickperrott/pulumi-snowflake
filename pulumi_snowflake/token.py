class Token:
    def __init__(self, sql):
        self.sql = sql

    def as_dict(self):
        return {
            "__token": self.sql
        }

def token_equal(self, other):
    if isinstance(other, Token):
        return other.sql == self.sql
    return False

Token.__eq__ = token_equal
