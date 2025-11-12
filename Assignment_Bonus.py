import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()

        if users:
            i = 0
            while i < len(users):
                user = users[i]
                name = user.get("name", "N/A")
                username = user.get("username", "N/A")
                email = user.get("email", "N/A")
                city = user.get("address", {}).get("city", "N/A")

                if city.lower().startswith('s'):
                    print(f"User {i+1}:")
                    print(f"Name: {name}")
                    print(f"Username: {username}")
                    print(f"Email: {email}")
                    print(f"City: {city}")
                    print("------------------------")

                i += 1
        else:
            print("No users found!")
    else:
        print("Failed to fetch data from API. Status Code:", response.status_code)

except Exception as e:
    print("An error occurred:", e)
