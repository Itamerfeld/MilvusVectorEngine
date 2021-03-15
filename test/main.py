from nose.tools import assert_true
import requests
from PIL import Image


#  CD root Folder & Run "nosetests --verbosity=2 main"

collection_name = 'test'


def test_create():
    response = requests.get(
        'http://localhost:5000/create_collection/'+collection_name+'?key=secret')
    assert_true(response.ok)


def test_info():
    response = requests.get(
        'http://localhost:5000/info_collection/'+collection_name+'?key=secret')
    assert_true(response.ok)


def test_drop():
    response = requests.get(
        'http://localhost:5000/drop_collection/'+collection_name+'?key=secret')
    assert_true(response.ok)
