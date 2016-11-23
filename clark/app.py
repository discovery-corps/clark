import falcon

from clark.controllers import root
from clark.controllers import torrents
from clark.middleware.authentication import auth_middleware

api = falcon.API(before=[auth_middleware])
api.req_options = True

root = root.Resource()
torrents = torrents.Resource()

api.add_route('/', root)
api.add_route('/torrents', torrents)
