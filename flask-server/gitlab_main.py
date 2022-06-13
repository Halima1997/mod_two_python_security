import requests
from requests.structures import CaseInsensitiveDict



def gitlab_request(project_id):
    url = "https://gitlab.com/api/v4/projects/" + str(project_id) + "/members"
    headers = CaseInsensitiveDict()
    headers["PRIVATE-TOKEN"] = "glpat-ESzjDzx8VgPxNvZ4VXbR"
    resp = requests.get(url, headers=headers)

    return resp


def getUsernames(project_id):
    response = gitlab_request(project_id)
    data = response.json()
    status = response.status_code
    if status == 200:
        usernames = [user['username'] for user in data]
        #print(usernames)
    return usernames




def user_ids(project_id):
    response = gitlab_request(project_id)
    data = response.json()
    status = response.status_code
    new_list = []

    if status == 200:
        for user in data:
            new_list.append(user['id'])
    return new_list
