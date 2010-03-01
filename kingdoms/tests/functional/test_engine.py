from kingdoms.tests import *

class TestEngineController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='engine', action='index'))
        # Test response...
