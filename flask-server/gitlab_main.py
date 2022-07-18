import requests
from requests.structures import CaseInsensitiveDict
class projectException(Exception):
    pass


def gitlab_projectid(project_id):
    url = "https://gitlab.com/api/v4/projects/" + str(project_id) + "/members"
    headers = CaseInsensitiveDict()
    headers["PRIVATE-TOKEN"] = "glpat-ESzjDzx8VgPxNvZ4VXbR"
    resp = requests.get(url, headers=headers)

    return resp

def gitlab_username(user_id):
    url = "https://gitlab.com/api/v4/users/" + str(user_id) + "/projects"
    headers = CaseInsensitiveDict()
    headers["PRIVATE-TOKEN"] = "glpat-ESzjDzx8VgPxNvZ4VXbR"
    resp = requests.get(url, headers=headers)

    return resp

 

def getUsernames(project_id):
    response = gitlab_projectid(project_id)
    data = response.json()
    status = response.status_code
    if status == 200:
        usernames = [user['username'] for user in data]
    
    if status == 404:
       raise projectException
    else:
        return usernames

def getProjectID(user_id):
    response = gitlab_username(user_id)
    data = response.json()
    status = response.status_code
    if status == 200:
        ids = [user['id'] for user in data]
    
    if status == 404:
       raise projectException
    else:
        return ids
