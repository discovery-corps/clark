from clark.objects import base


class Torrent(base.BaseObject):
    @classmethod
    def list(cls):
        torrents = []  # TODO db.get_torrents()
        torrents = [cls.from_db(t) for t in torrents]
        return torrents
