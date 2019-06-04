import sys
import os
from github import Github

# Path to the folder you want to store projects in
path = "~/Desktop/Programming/Projects/"

# Enter your Github username and password here
username = ""
password = ""

def create():
    user = Github(username, password).get_user()
    user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))

if (__name__ == "__main__"):
    create()