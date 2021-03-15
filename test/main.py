from nose.tools import assert_true
import requests
from PIL import Image


#  CD root Folder & Run "nosetests --verbosity=2 main"

def config():
    return{
        "API_CREATE": "http://localhost:5000/create_collection/",
        "API_INFO": "http://localhost:5000/info_collection/",
        "API_DROP": "http://localhost:5000/drop_collection/",
        "API_KEY": "?key=secret"
    }


collection_name = 'test'
config = config()


def test_create():
    response = requests.get(
        config['API_CREATE']+collection_name + config['API_KEY'])
    assert_true(response.ok)


def test_info():
    response = requests.get(
        config['API_INFO']+collection_name + config['API_KEY'])
    assert_true(response.ok)


def test_drop():
    response = requests.get(
        config['API_DROP']+collection_name + config['API_KEY'])
    assert_true(response.ok)
