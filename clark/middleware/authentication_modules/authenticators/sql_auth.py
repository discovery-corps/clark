from clark.objects.users import users
from sqlalchemy.sql import select
from sqlalchemy import create_engine
from clark.objects.users import User
import talons


engine = create_engine('sqlite://:memory:')
conn = engine.connect()


class SQLIdentifier(talons.auth.interfaces.Identifies):

    def __init__(self):
        super().__init__()
        pass

    def identify(self, request):
        username = request.get_param('username')
        if username
            selections = select([users]).where(users.c.username == username)
            selections = conn.execute(selections)
            user = selections.fetchone()
            if user:
                user = User(username, password=password)
                return user
        return False

class SQLAuthenticator(talons.auth.interfaces.Authenticates):

    def __init__(self):
        super().__init__()
        pass

    def authenticate(self, identity):
        return identity.authenticate()

