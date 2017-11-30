from unittest import TestCase
from unittest.mock import Mock, patch
from nose.tools import nottest
import json

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

        mock_get.return_value = "blah"

        # print(mock_get.return_value)

        result = norris.get_joke()

        # print(result)

        self.assertEqual(self.test_response, result)

    # @nottest
    @patch('norris.services.get_joke')
    def test_norris_value(self, mock_get):

        mock_get.return_value = self.test_response

        print(mock_get)

        result = norris.joke_length()
        self.assertEqual(result, len( "Chuck Norris broke the speed of sound. With his elbow." ) )