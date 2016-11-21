import json

import falcon

from clark.hooks import permissions as permission_hooks
from clark import objects


class Resource(object):
    @falcon.before(permission_hooks.view_torrents)
    def on_get(self, req, resp):
        torrents = objects.Torrent.list()
        resp.body = json.dumps({'torrents': torrents})
        resp.status = falcon.HTTP_OK
