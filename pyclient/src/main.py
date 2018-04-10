#! /usr/bin/env python
from mud1 import gmain2

def main():
    user = { 'username': "User" }
    gmain2.main(user, filename="mud.1", n="NewUser")


if __name__ == '__main__':
    main()
