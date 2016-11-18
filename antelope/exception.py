import falcon


class HTTPForbidden(falcon.HTTPForbidden):
    title = None
    description = None

    def __init__(self, title=None, description=None, **kwargs):
        super(HTTPForbidden, self).__init__(title or self.title,
                                            description or self.description,
                                            **kwargs)


class CannotViewTorrentsError(HTTPForbidden):
    title = 'Permission Denied'
    description = 'You do not have permission to view torrents'
