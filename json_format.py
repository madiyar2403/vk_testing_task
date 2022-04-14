from datetime import date


def get_json(user):
    """Returns a list of friends for further report generation in json format

    Args:
        user (dict): contains information about the user's friends

    Returns:
        json_data: a sorted by first_name list containing a dictionary about the user's friends with the
                   required keys and values
    """

    json_keys = ['first_name', 'last_name', 'country', 'city', 'birth_date', 'sex']
    json_data = []

    for friend in user:
        first_name = friend.get('first_name')
        last_name = friend.get('last_name')
        sex = friend.get('sex')
        country = friend.get('country', {}).get('title')
        city = friend.get('city', {}).get('title')
        bdate = friend.get('bdate')
        try:
            date.isoformat(bdate)
        except TypeError:
            pass

        dict_friends = {json_keys[0]: first_name, json_keys[1]: last_name, json_keys[2]: country,
                        json_keys[3]: city, json_keys[4]: bdate, json_keys[5]: 'female' if int(sex) == 1 else 'male'}

        json_data.append(dict_friends)

    return sorted(json_data, key=lambda d: d['first_name'])
