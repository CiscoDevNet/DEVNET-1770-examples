from unittest import TestCase
from unittest.mock import patch
from nose.tools import nottest

import norris

"""
Response will look something like this
{
  "category": "['science']",
  "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
  "id": "7SIYDCQ6QiiTLtd-B3sBEQ",
  "url": "http://api.chucknorris.io/jokes/7SIYDCQ6QiiTLtd-B3sBEQ",
  "value": "Chuck Norris broke the speed of sound. With his elbow."
}
"""

class TestNorris(TestCase):

    # setup and teardown

    def setUp(self):
        self.test_response = {
            "category": "['science']",
            "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
            "id": "7SIYDCQ6QiiTLtd-B3sBEQ",
            "url": "http://api.chucknorris.io/jokes/7SIYDCQ6QiiTLtd-B3sBEQ",
            "value": "Chuck Norris broke the speed of sound. With his elbow."
        }


    # @nottest
    def test_norris_basic(self):

        result = norris.get_joke()
        print("TEST_RESPONSE: " + self.test_response["value"])
        print("RESULT: " + result["value"])
        self.maxDiff = None
        # This will always fail because the API brings back a different response each time
        self.assertEqual(result, self.test_response)

    # Create a mocked test case so that you can test app functionality, not the API itself
    # @nottest
    @patch('norris.get_joke')
    def test_norris_mock(self, mock_get):
        mock_response = {
            "category": "['science']",
            "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
            "id": "7SIYDCQ6QiiTLtd-B3sBEQ",
            "url": "http://api.chucknorris.io/jokes/7SIYDCQ6QiiTLtd-B3sBEQ",
            "value": "Chuck Norris broke the speed of sound. With his elbow."
        }

        mock_get.return_value = mock_response

        result = norris.get_joke()

        self.assertEqual(mock_response, result)

    # @nottest
    @patch('norris.services.get_joke')
    def test_norris_value(self, mock_get):

        mock_response2 = {
            "category": "['science']",
            "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
            "id": "7SIYDCQ6QiiTLtd-B3sBEQ",
            "url": "http://api.chucknorris.io/jokes/7SIYDCQ6QiiTLtd-B3sBEQ",
            "value": "Chuck Norris broke the speed of sound. With his elbow."
        }

        mock_get.return_value = mock_response2

        result = norris.joke_length()
        self.assertEqual(result, len( "Chuck Norris broke the speed of sound. With his elbow." ) )