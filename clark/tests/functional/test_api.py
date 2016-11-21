import multiprocessing
import unittest
from wsgiref import simple_server

import requests

from clark import app


class Server(object):
    def start(self):
        server = simple_server.make_server('', 8000, app.api)
        self.process = multiprocessing.Process(target=server.serve_forever,
                                               name='test-server')
        self.process.daemon = True
        self.process.start()
        self.process.join(1)

    def stop(self):
        self.process.terminate()


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.server = Server()
        self.server.start()

    def tearDown(self):
        self.server.stop()

    def test_get_root(self):
        r = requests.get('http://localhost:8000/')
        print(r.headers)
        self.assertEqual(r.json(), {'hello': 'world'})
