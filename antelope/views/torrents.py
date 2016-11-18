import json

import falcon

from antelope.hooks import permissions as permission_hooks


class Resource(object):
    @falcon.before(permission_hooks.view_torrents)
    def on_get(self, req, resp):
        torrents = {'torrents': []}
        resp.body = json.dumps(torrents)
        resp.status = falcon.HTTP_OK
