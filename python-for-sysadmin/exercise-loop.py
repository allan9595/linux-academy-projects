#!/usr/bin/env python3.6
users = [
        {'admin': False, 'active': True, 'name':'allan'},
        {'admin': True, 'active': True, 'name':'Bob'},
        {'admin': False, 'active': False, 'name': 'Alice'},
        {'admin': False, 'active': True, 'name':'Jack'}
]

for user in users:
    if user['admin'] == True:
        print(f"{users.index(user)+1} (ADMIN) {user['name']}")
    elif user['active'] == True:
        print(f"{users.index(user)+1} ACTIVE - {user['name']}")
    elif user['admin'] == True and user['active'] == True:
        print(f"{users.index(user)+1} ACTIVE - (ADMIN) {user['name']}")
    else:
        print(f"{users.index(user)+1} {user['name']}")
