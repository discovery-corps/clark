from antelope import objects
from antelope.tests.unit import base


class TestTorrents(base.Base):
    def test_list(self):
        self.assertEqual([], objects.Torrent.list())
