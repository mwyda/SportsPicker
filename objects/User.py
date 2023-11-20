from objects import MetaUser


class User:
    __metaclass__ = MetaUser

    def __init__(self, username, hashedPass, salt, firstName, lastName, email, userId=-1, phoneNumber="", ):
        self.username = username
        self.hashedPass = hashedPass
        self.salt = salt
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userId = userId
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"User: {self.username}"
