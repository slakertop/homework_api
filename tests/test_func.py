import requests


def test_func(url, status_code):
    r = requests.get(url)
    print(url, status_code)
    assert r.status_code == int(status_code)
