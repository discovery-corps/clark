import random

from antelope import exception


def view_torrents(req, resp, resource, params):
    # TODO use this when we have a permissions system
    # if not params['user'].has_permission('torrents:view'):
    if random.randint(1, 2) == 2:
        raise exception.CannotViewTorrentsError
