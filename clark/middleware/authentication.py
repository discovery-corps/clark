from talons.auth import middleware
from talons.auth import basicauth, httpheader, htpasswd
import clark.configuration


config = clark.configuration.load_auth_config()
auth_middleware = middleware.create_middleware(**config)
