import json
from argparse import Namespace


class BaseConfig:

    def __init__(self, path):
        self.path = path
        self.config = False
        self.load()

    def load(self):
        with open(self.path) as data_in:
            self.config = json.load(data_in,
                                    object_hook=lambda d: Namespace(**d))


class ModuleConfig(BaseConfig):

    def __init__(self, path, root_config):
        super().__init__(path)
        self.config = root_config
        self.load()
