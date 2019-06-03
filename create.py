import sys
import os
from github import Github

path = "~/Desktop/Programming/Projects/"

username = "JSLeadbetter"
password = "88c70d451b17f9be8378959014501974100c41e5"

def create():
    user = Github(username, password).get_user()
    user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))

if (__name__ == "__main__"):
    create()