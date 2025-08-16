from http.client import responses

import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers)
    print(response.status_code)
    print(response.text)
    return response

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

