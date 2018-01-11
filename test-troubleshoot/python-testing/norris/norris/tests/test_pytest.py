import pytest
import responses

from norris import get_joke, joke_length

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

@pytest.fixture
def my_responses():

    test_response = {
        "category": ['science'],
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "id": "7SIYDCQ6QiiTLtd-B3sBEQ",
        "url": "http://api.chucknorris.io/jokes/7SIYDCQ6QiiTLtd-B3sBEQ",
        "value": "Chuck Norris broke the speed of sound. With his elbow."
    }

    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'https://api.chucknorris.io/jokes/random?category=science',
                 json=test_response, status=200)
        yield rsps


def test_pytest_norris_basic(my_responses):
    verify_response = {
        "category": ['science'],
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "id": "7SIYDCQ6QiiTLtd-B3sBEQ",
        "url": "http://api.chucknorris.io/jokes/7SIYDCQ6QiiTLtd-B3sBEQ",
        "value": "Chuck Norris broke the speed of sound. With his elbow."
    }
    result = get_joke()
    assert result == verify_response


def test_norris_value(my_responses):

    test_value = len("Chuck Norris broke the speed of sound. With his elbow.")
    # test_value = 5

    result = joke_length()
    assert result == test_value

# This test is to demonstrate when you might want to use curl or postman
# to troubleshoot an API call
"""
Imagine the response used to look like:
{
  "data": {
      "category": "['science']",
      "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
      "id": "7SIYDCQ6QiiTLtd-B3sBEQ",
      "url": "http://api.chucknorris.io/jokes/7SIYDCQ6QiiTLtd-B3sBEQ",
      "value": "Chuck Norris broke the speed of sound. With his elbow."
  }
}
"""
def test_norris_badkey():
    result = get_joke()
    # This will fail because there's no such key as data anymore
    assert result["data"]["value"] == "This is a bad key"
