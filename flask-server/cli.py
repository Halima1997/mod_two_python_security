import argparse
from gitlab_main import usernames, user_ids

parser = argparse.ArgumentParser(description="Add project ID")
parser.add_argument("-p", "--project_id", metavar='project_id', type=str, help='enter your project_id')
args = parser.parse_args()


def project_username(project_id):
    users = usernames(project_id)
    for user in users:
        print(user)


def project_user_id(project_id):
    users = user_ids(project_id)
    for user in users:
        print(user)


project_username(args.project_id)
project_user_id(args.project_id)
