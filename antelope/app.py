import falcon

from antelope.views import root
from antelope.views import torrents


api = falcon.API()

root = root.Resource()
torrents = torrents.Resource()

api.add_route('/', root)
api.add_route('/torrents', torrents)
