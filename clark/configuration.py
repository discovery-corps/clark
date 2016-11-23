import json


def load_auth_config(location="auth_config.json"):
    config = json.loads(location)
    return config
