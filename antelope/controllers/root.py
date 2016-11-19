import json

import falcon


class Resource(object):
    def on_get(self, req, resp):
        resp.body = json.dumps({'hello': 'world'})
        resp.status = falcon.HTTP_OK
