from kingdoms.tests import *

class TestMapController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='map', action='index'))
        # Test response...
