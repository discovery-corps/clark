from clark.objects import base
from sqlalchemy import Sequence, Table, Column, Integer, String


users = Table('users', metadata,
              Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
              Column('username', String(50)),
              Column('password', String(50))
              )


class User(base.BaseObject):

    def __init__(self, username, password=None):
        pass

    def authenticate(self, password):
        pass
