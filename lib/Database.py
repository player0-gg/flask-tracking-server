from flask import g


def _get_client():
    if not hasattr(g, 'client'):
        # TODO: init client mysql, mongodb, ...
        client = "TODO"
        g.client = client

    return client


def update(user, data):
    client = _get_client()
    pass


def upload(user, data):
    client = _get_client()
    pass


