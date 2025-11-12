import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    if users:
        i = 0
        while i < len(users):
            user = users[i]
            name = user.get("name")
            username = user.get("username")
            email = user.get("email")
            city = user.get("address").get("city")
            print(f"User {i+1}:")
            print(f"Name: {name}")
            print(f"Username: {username}")
            print(f"Email: {email}")
            print(f"City: {city}")
            print("------------------------")
            i+=1
    else:
        print("No users found!")
