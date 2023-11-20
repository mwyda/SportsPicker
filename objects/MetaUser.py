import database.CRUD as db


class MetaUser:

    def __call__(self, username):
        user = db.getUser(username)
        if not user:
            '''Not in the database so create it'''
            user = type.__call__(self, username)
        return user
