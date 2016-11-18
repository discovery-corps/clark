import falcon

from antelope.views import torrents


api = falcon.API()

torrents = torrents.Resource()
api.add_route('/torrents', torrents)
