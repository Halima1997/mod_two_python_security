import requests
from requests.structures import CaseInsensitiveDict


def _original_request(project_id):
    url = "https://gitlab.com/api/v4/projects/32801417/members"
    headers = CaseInsensitiveDict()
    headers["PRIVATE-TOKEN"] = "glpat-ESzjDzx8VgPxNvZ4VXbR"
    resp = requests.get(url, headers=headers)

    return resp

#remove project id from here

def status_code(project_id):
    response = _original_request(project_id)

    return response.status_code

def username(project_id):
    response = _original_request(project_id)
    data = response.json()

    for user in data:
        return (user['username'])

    return (username(32801417))


def user_id(project_id):
    response = _original_request(project_id)
    data = response.json()

    for user in data:
        print(user['id'])
user_id(32801417)
