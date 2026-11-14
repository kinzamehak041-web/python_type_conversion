import requests
try:

    url=input("Enter a valid URL: ")
    response = requests.get(url,timeout=10)

    print(response.ok)
    print(response.status_code)
except requests.exceptions,RequestException:

    print("plaese enter a valid url")

import requests
import json
try :
    user_name=input("Enter youe user name: ")

    url = "https://api.github.com/users/"+user_name

    response = requests.get(url,timeout=10)
    my_dict=response.json()
    print(my_dict["login"])
    print(my_dict["public_repos"]) 
    print(my_dict["followers"])
    print(my_dict["html_url"])
except requests.exceptions.RequestException as e:
    print("Request error:", e)


