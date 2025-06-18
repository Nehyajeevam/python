import json

with open('emp.json', 'r') as fp1, open('users.json', 'w') as fp2:
    users = json.load(fp1)
    print(type(users))
    json.dump(users, fp2)
    print("new file created!")