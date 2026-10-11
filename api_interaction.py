import requests
def fetch_and_display_users(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        user = response.json()
        print("Name:", user["name"])
        print("Username:", user["username"])
        print("Email:",user["email"])
    else:
        print("Failed to fetch user. Status code:", response.status_code)

fetch_and_display_users(4)
fetch_and_display_users(16)