from nose.tools import assert_true
import requests


def config():
    return{
        "API_CREATE": "http://localhost:5000/create_collection/",
        "API_INFO": "http://localhost:5000/info_collection/",
        "API_DROP": "http://localhost:5000/drop_collection/",
        "API_INSERT": "http://localhost:5000/insert_collection/",
        "API_SEARCH": "http://localhost:5000/search_collection/",
        "FILE_PATH": "./test.jpeg",
        "API_KEY": "?key=secret"
    }


collection_name = 'test'
config = config()


def test_create():
    url = config['API_CREATE']+collection_name + config['API_KEY']
    response = requests.get(url)
    assert_true(response.ok)


def test_info():
    url = config['API_INFO']+collection_name + config['API_KEY']
    response = requests.get(url)
    assert_true(response.ok)


def test_insert():
    url = config['API_INSERT'] + config['API_KEY']
    payload = {'collection_name': collection_name}
    files = [('file', open(config['FILE_PATH'], 'rb'))]
    response = requests.request(
        "POST", url, headers={}, data=payload, files=files)
    assert_true(response.ok)


def test_search():
    url = config['API_SEARCH'] + config['API_KEY']
    payload = {'collection_name': collection_name}
    files = [('file', open(config['FILE_PATH'], 'rb'))]
    response = requests.request(
        "POST", url, headers={}, data=payload, files=files)
    assert_true(response.ok)


def test_drop():
    url = config['API_DROP']+collection_name + config['API_KEY']
    response = requests.get(url)
    assert_true(response.ok)
