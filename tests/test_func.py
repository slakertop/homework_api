import requests


def test_func(url, status_code):
    try:
        r = requests.get(url)
        assert r.status_code == int(status_code)
    except requests.exceptions.ConnectionError as err:
        assert 404 == int(status_code)
