#!/usr/bin/env python3.6
user = {'admin': True, 'active': True, 'name':'allan'}

if user['admin'] and not user['active']:
    print(f"(ADMIN) {user['name']}")
elif user['active'] and not user['admin']:
    print(f"ACTIVE {user['name']}")
elif user['admin'] and user['active']:
    print(f"ACTIVE - (ADMIN) {user['name']}")
else:
    print(user['name'])

//
