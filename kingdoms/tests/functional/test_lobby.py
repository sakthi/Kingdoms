from kingdoms.tests import *

class TestLobbyController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='lobby', action='index'))
        # Test response...
