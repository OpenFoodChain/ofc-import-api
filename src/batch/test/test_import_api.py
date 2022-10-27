import pytest
import requests
import random
import string
import os
import json
from datetime import date, timedelta

pytest.url = 'http://localhost:8777/'
#'http://' + str(os.environ.get('IMPORT_API_HOST')) + ':' + str(os.environ.get('IMPORT_API_PORT')) + '/'
 
pytest.today = (date.today()).isoformat()
pytest.next_week = (date.today() + timedelta(days=7)).isoformat()
pytest.bbd = (date.today() + timedelta(days=14)).isoformat()
pytest.country = 'Amsterdam ' + str(random.randint(1, 200))

print(pytest.url)

def randomize(length):
	random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
	return random_string

def random_int(length):
	random_int = str(random.randint(1, length))
	return random_int

def test_batch_import_get():
	response = requests.get(pytest.url + 'batch/import')
	assert response.status_code == 200

def test_batch_import_integrity_get():
    response = requests.get(pytest.url + 'batch/import-integrity/')
    assert response.status_code == 200

def test_batch_import_tstx_get():
    response = requests.get(pytest.url + 'batch/import-tstx/')
    assert response.status_code == 200

def test_batch_import_post():
    values = {
        "anfp": "anfp" + randomize(4),
        "dfp": "dfp" + randomize(5),
        "bnfp": "bnfp" + randomize(4),
        "pds": pytest.today,
        "pde": pytest.next_week,
        "jds": random_int(3),
        "jde": random_int(3),
        "bbd": pytest.bbd,
        "pc": randomize(3),
        "pl": "pl" + randomize(5),
        "rmn": "rmn" + randomize(5),
        "pon": "pon" + randomize(5),
        "pop": randomize(3),
        "mass": random_int(4),
        "raw_json": {}
    }
    
    response = requests.post(pytest.url + 'batch/import/', data = values)
    assert response.status_code == 201

def test_batch_import_integrity_post():
    response = requests.get(pytest.url + 'batch/import')
    data=json.loads(response.text)

    values = {
        "integrity_address": pytest.country,
        "integrity_pre_tx": randomize(40),
        "integrity_post_tx": randomize(40),
        "batch": data[-1]['id'],
        "batch_lot_raddress": randomize(20),
        "offline_wallet_sent": {}
    }

    response = requests.post(pytest.url + 'batch/import-integrity/', data = values)
    assert response.status_code == 201

def test_batch_import_tstx_post():
    response = requests.get(pytest.url + 'batch/import')
    data = json.loads(response.text)

    values = {
        "sender_raddress": randomize(34),
        "sender_name": randomize(20),
        "tsintegrity": data[-1]['integrity_details']['id'],
        "txid": randomize(64)
    }

    response = requests.post(pytest.url + 'batch/import-tstx/', data = values)
    assert response.status_code == 201