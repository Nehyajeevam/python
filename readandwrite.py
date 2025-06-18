import requests,json
api_url='https://jsonplaceholder.typicode.com/users'

data=requests.get(api_url)
users=data.json()
print(type(users))  #<class,list />

with open('new_users.json', 'w', encoding='utf-8') as fp:
	json.dump(users, fp, ensure_ascii=False)

print("New file Created!")