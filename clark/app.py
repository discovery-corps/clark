import falcon

from clark.controllers import root
from clark.controllers import torrents


api = falcon.API()

root = root.Resource()
torrents = torrents.Resource()

api.add_route('/', root)
api.add_route('/torrents', torrents)
