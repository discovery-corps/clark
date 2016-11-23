from clark.objects.torrents import Torrent
from clark.objects.users import User
from sqlalchemy import MetaData
__all__ = [
    'Torrent',
    'User'
]

metadata = MetaData()