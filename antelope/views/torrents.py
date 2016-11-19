import json

import falcon

from antelope.hooks import permissions as permission_hooks
from antelope import objects


class Resource(object):
    @falcon.before(permission_hooks.view_torrents)
    def on_get(self, req, resp):
        torrents = objects.Torrent.list()
        resp.body = json.dumps({'torrents': torrents})
        resp.status = falcon.HTTP_OK
