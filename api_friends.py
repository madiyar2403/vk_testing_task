import requests

TOKEN = "token"


def get_user_friends():
    """Makes a request to Vk API and returns response

    Returns:
        res: a list containing dictionaries of user's friends
    """

    while True:
        try:
            user_id_input = int(input("Please, enter user id:"))
            res = requests.get("https://api.vk.com/method/friends.get", params={
                "user_id": user_id_input,
                "fields": "country, city, bdate, sex",
                "access_token": TOKEN,
                "v": 5.122
            }).json()["response"]["items"]
            return res

        except ValueError:
            print('Please, enter correct user id')
        except KeyError:
            print('User with this id not found')
